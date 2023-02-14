alltext = open("stringchange.txt", "r+")
print(alltext.readable())
newtext = open("newchanged.txt", "w")
for employee in alltext.readlines():
    x = employee.replace("Change Me", "To This")
    # replace "TEXT TO CHANGE"
    # The second "" can be entered with a different string, and it will replace the first string for the second
    # x = employee.replace("TEXT TO CHANGE","Apple") --> "Apple" will replace "TEXT TO CHANGE"

    newtext.write(x)
    print(x)

alltext.close()
newtext.close()
