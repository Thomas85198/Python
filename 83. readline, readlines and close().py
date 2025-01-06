file = open("myFile.txt")

while True:
    line = file.readline()
    if not line:
        break
    else:
        print(line)

file.close()
