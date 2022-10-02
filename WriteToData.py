import requests
from Config import API_KEY

BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'


def writeData(name_tables, cursor, data, data_type):
    if data_type == 1:
        writeDataType1(name_tables, cursor, data)
    elif data_type == 2:
        writeDataType2(name_tables, cursor, data)
    elif data_type == 3:
        writeDataType3(name_tables, cursor, data)
    elif data_type == 4:
        writeDataType4(name_tables, cursor, data)
    elif data_type == 5:
        writeDataType5(name_tables, cursor, data)
    elif data_type == 6:
        writeDataType6(name_tables, cursor, data)
    elif data_type == 7:
        writeDataType7(name_tables, cursor, data)
    elif data_type == 8:
        writeDataType8(name_tables, cursor, data)
    elif data_type == 9:
        writeDataType9(name_tables, cursor, data)
    elif data_type == 10:
        writeDataType10(name_tables, cursor, data)
    elif data_type == 11:
        writeDataType11(name_tables, cursor, data)
    elif data_type == 12:
        writeDataType12(name_tables, cursor, data)
    elif data_type == 13:
        writeDataType13(name_tables, cursor, data)
    elif data_type == 14:
        writeDataType14(name_tables, cursor, data)
    elif data_type == 15:
        writeDataType15(name_tables, cursor, data)
    elif data_type == 16:
        writeDataType16(name_tables, cursor, data)
    elif data_type == 17:
        writeDataType17(name_tables, cursor, data)


def getLatLng(address):
    endpoint = f"{BASE_URL}?address={address}&key={API_KEY}"
    r = requests.get(endpoint)
    lat, lng = 0.00, 0.00
    if r.status_code in range(200, 299):
        results = r.json()['results'][0]
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
    return lat, lng


def writeDataType1(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[3]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `description`, `location`, " \
                                                  "`initial_price`, `monthly_payment`, `link`, `coordinatesX`, " \
                                                  "`coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  str(data[6]), lat, lng))


def writeDataType2(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[3]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `description`, `location`, " \
                                                  "`object`, `initial_price`, `link`, `coordinatesX`, " \
                                                  "`coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  str(data[6]), lat, lng))


def writeDataType3(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[3]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `description`, `location`, " \
                                                  "`square`, `initial_price`, `link`, `coordinatesX`, " \
                                                  "`coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  str(data[6]), lat, lng))


def writeDataType4(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[2]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `location`, `square`, " \
                                                  "`description`, `initial_price`, `term` ,`link`, `coordinatesX`, " \
                                                  "`coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  str(data[6]), str(data[7]), lat, lng))


def writeDataType5(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[4]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `fossil`, `name`, " \
                                                  "`location`, `work`, `link`, `coordinatesX`, " \
                                                  "`coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  str(data[6]), lat, lng))


def writeDataType6(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[0]))

    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `location`, `number`, `object`, " \
                                                  "`term`, `link`, `coordinatesX`, " \
                                                  "`coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]),
                                  lat, lng))


def writeDataType7(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[2]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `location`, `square`, " \
                                                  "`object`, `initial_price`, `link`, `coordinatesX`, " \
                                                  "`coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  str(data[6]), lat, lng))


def writeDataType8(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[5]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `description`, `initial_price`, " \
                                                  "`object`, `location`, `link`, `coordinatesX`, " \
                                                  "`coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  str(data[6]), lat, lng))


def writeDataType9(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[0]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `location`, `description`, " \
                                                  "`object`, `transmission_methods`, `initial_price`, `link`, " \
                                                  "`coordinatesX`, `coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, " \
                                                  "%s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[0]), str(data[2]), str(data[3]), str(data[4]),
                                  str(data[5]), str(data[6]), lat, lng))


def writeDataType10(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[2]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `location`, `object`, " \
                                                  "`initial_price`, `link`, `coordinatesX`, `coordinatesY`) " \
                                                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  lat, lng))


def writeDataType11(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[3]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `object`, `location`, " \
                                                  "`initial_price`, `link`, `coordinatesX`, `coordinatesY`) " \
                                                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  lat, lng))


def writeDataType12(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[4]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `term`, `services`, " \
                                                  "`location`, `initial_price`, `object`, `link`, " \
                                                  "`coordinatesX`, `coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, " \
                                                  "%s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  str(data[6]), str(data[7]), lat, lng))


def writeDataType13(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[4]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `description`, `initial_price`, " \
                                                  "`location`, `link`, `coordinatesX`, " \
                                                  "`coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  lat, lng))


def writeDataType14(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[2]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `location`, `description`, " \
                                                  "`initial_price`, `term`, `link`, `coordinatesX`, " \
                                                  "`coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  str(data[6]), lat, lng))


def writeDataType15(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[3]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `description`, `location`, " \
                                                  "`initial_price`, `monthly_payment`, `link`, `coordinatesX`, " \
                                                  "`coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  str(data[6]), lat, lng))


def writeDataType16(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[3]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `description`, `location`, " \
                                                  "`initial_price`, `link`, `coordinatesX`, `coordinatesY`) VALUES (" \
                                                  "%s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  lat, lng))


def writeDataType17(name_tables, cursor, data):
    lat, lng = getLatLng(str(data[5]))
    insert_query = "INSERT INTO " + name_tables + "(`organizers`, `number`, `object`, `description`, " \
                                                  "`initial_price`, `location`, `link`, `coordinatesX`, " \
                                                  "`coordinatesY`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
    cursor.execute(insert_query, (str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]),
                                  str(data[6]), lat, lng))
