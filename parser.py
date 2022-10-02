from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import openpyxl
import os
from openpyxl.writer.excel import save_workbook
from selenium.webdriver.common.by import By

from Config import host, user, password, db_name, port
import WriteToData
import time
import pymysql

URL = "https://torgi.gov.ru/lotSearch2.html?bidKindId="
FILE_DATA = "elements.xlsx"
EXE_PATH = "chromedriver.exe"
FILTER_FOR_SEARCH = "https://torgi.gov.ru/lotSearch2.html"
TYPE_COUNT = 17


def get_pages_count(html):
    pagination = html.find_elements(By.XPATH, "//a[@title='Перейти на последнюю страницу']")
    if pagination and pagination[0].text != '':
        return int(pagination[0].text)
    pagination = html.find_elements(By.XPATH, "//tr[@class='navigation']/td/div/span")
    if pagination:
        return int(pagination[-1].text)
    return 1


def get_data(html):
    result = []
    for i in range(1, len(html)):
        result.append(html[i].text)
    x = html[0].find_elements(By.XPATH, "span")[0].find_elements(By.XPATH, "div")[0].find_elements(By.XPATH, "a")[
        1].get_attribute("href")
    result.append(x)
    return result


def get_writer_data(html):
    result = []
    for i in range(0, len(html)):
        result.append(html[i])
    return result


def get_content(html):
    items = html.find_elements(By.XPATH, "//tr[@class='even datarow']")
    items += html.find_elements(By.XPATH, "//tr[@class='odd datarow']")
    elements = []
    for item in items:
        data = get_data(item.find_elements(By.XPATH, "td"))
        elements.append(data)
    return elements


def init_driver():
    service = Service(str(EXE_PATH))
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options, service=service)
    driver.set_window_size(1440, 900)
    return driver


def save_data(items, driver, index):
    try:
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        try:
            with connection.cursor() as cursor:
                name_tables = "tablestype" + str(index)
                clear_table_query = "DELETE FROM " + name_tables + ";"
                clear_id_query = "ALTER TABLE " + name_tables + " AUTO_INCREMENT=0;"
                cursor.execute(clear_table_query)
                cursor.execute(clear_id_query)
                for item in items:
                    data = get_writer_data(item)
                    WriteToData.writeData(name_tables, cursor, data, index)
                connection.commit()
                print("Commit done...")
        finally:
            connection.close()
    except Exception as ex:
        print("Connection refused...")
        print(ex)


def is_exists(driver):
    try:
        wait_to_load = driver.find_elements(By.XPATH, "//div[@class='over'] [@style='display: none;']")
    except NoSuchElementException:
        return []
    return wait_to_load


def loading(driver):
    while len(is_exists(driver)) == 0:
        time.sleep(0.26)


def select_filter(driver, index):
    driver.get(URL + str(index))
    driver.get(FILTER_FOR_SEARCH)


def next_page(page, page_count, driver):
    if page != page_count:
        driver.find_element(By.XPATH, "//a[@title='Перейти на одну страницу вперед']").click()
        loading(driver)


def parse():
    driver = init_driver()
    for index in range(1, TYPE_COUNT + 1):
        elements = []
        select_filter(driver, index)
        page_count = get_pages_count(driver)
        # limited pages
        for page in range(1, min(page_count + 1, 20)):
            print('pars: ', page, ' page in ', page_count, 'pages')
            elements.extend(get_content(driver))
            next_page(page, page_count, driver)
        save_data(elements, driver, index)


parse()
