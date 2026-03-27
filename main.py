# APIs import

# AssetManagement endpoints
from AssetsManagement.main import getAllDevices, getByAssetTag, getBySerialNumber, createDevice, updateDevice

continueVar = 1

while continueVar == 1:
    optionSelection = int(input("\n ***Options***\n\n 1) Create device \n 2) Modify existing device \n 3) Get device by asset tag \n 4) Get device by serial number \n 5) Get all existing devices \n 0) Close app  \n Type a number: "))
    match optionSelection:
        case 0: 
            continueVar = 0
        case 1:
            brand = input("Insert the brand: ")
            model = input("Insert the model: ")
            dType = input("Insert the type: ")
            aTag = input("Insert the asset tag: ")
            sNumber = input("Insert the serial number: ")
            print(createDevice(brand, model, dType, aTag, sNumber))
        case 2:
            brand = input("Insert the brand: ")
            model = input("Insert the model: ")
            dType = input("Insert the type: ")
            aTag = input("Insert the asset tag: ")
            sNumber = input("Insert the serial number: ")
            print(updateDevice(brand, model, dType, aTag, sNumber))

        case 3:
            assetNumber = input("Insert the asset tag you want to check: ")
            print(getByAssetTag(assetNumber))
        case 4: 
            serialNumber = input("Insert the serial number you want to check: ")
            print(getBySerialNumber(assetNumber))
        case 5:
            print(getAllDevices())
        case _:
            print("Select a valid option")

print("\n\n\nClosing app\n\n\n")