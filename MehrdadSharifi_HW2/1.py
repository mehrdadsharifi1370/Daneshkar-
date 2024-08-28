def Is_zipcode_valid(zipcode: str):
    if len(zipcode) == 11 and zipcode[5] == "-":
        return 1
    else:
        return 0


def spilit_input(*inserted_zipcode):
    Valid_zipcodes = []
    for index in range(len(inserted_zipcode)):
        if Is_zipcode_valid(inserted_zipcode[index]):
            Valid_zipcodes.append(inserted_zipcode[index])
        else:
            continue
    return Valid_zipcodes


print(spilit_input("12345-67890", "25454", "12345-67898"))
