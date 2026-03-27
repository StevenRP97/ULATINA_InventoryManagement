# Rerquired import and connection string 
import mysql.connector
from mysql.connector import Error
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="inventorymanagement"
)

# It gets device by asset tag
def getAllDevices():
    try: 
        connection.connect()
        result = []
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM devices;")
        for row in cursor:result.append(row)

    except Error as e:
        return "Database error: " + str(e)

    finally: 
        cursor.close()
        connection.close()

    return result

# It gets device by asset tag
def getByAssetTag(data):
    try: 
        connection.connect()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM devices WHERE assetTag = '{data}';")
        for row in cursor:result = row
    except Error as e: 
        return "Database error: " + str(e)
    finally: 
        cursor.close()
        connection.close()

    return result

# It gets device by asset tag
def getBySerialNumber(data):
    try: 
        connection.connect()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM devices WHERE serialNumber = '{data}';")
        for row in cursor:result = row

    except Error as e: 
        return "Database error: " + str(e)
    finally: 
        cursor.close()
        connection.close()
        
    return result

# It creates a new devices
def createDevice(brand, model, dType, aTag, sNumber):
    try: 
        connection.connect()
        cursor = connection.cursor()
        query = "INSERT INTO inventorymanagement.devices VALUES (%s, %s, %s, %s, %s, %s)"
        values = (brand, model, dType, aTag, sNumber, 0)
        cursor.execute(query,values)
        connection.commit()

    except Error as e:
        return "Database error: " + str(e)

    finally:
        cursor.close()
        connection.close()
    return "Created successfully"

# Endpoint to update a specific 
def updateDevice(brand, model, dType, aTag, sNumber):
    try: 
        connection.connect()
        cursor = connection.cursor()
        query = "UPDATE devices SET brand = %s, model = %s, type = %s, assetTag = %s, serialNumber = %s WHERE assetTag = %s"
        values = (brand, model, dType, aTag, sNumber, aTag)
        cursor.execute(query,values)
        connection.commit()
    except Error as e:
        return "Database error: " + str(e)

    finally: 
        cursor.close()
        connection.close()
    return "Updated successfully"
