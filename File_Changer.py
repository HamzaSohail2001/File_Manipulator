with open("example1.txt", "r") as file1:
    FileContent = file1.read()
    print(FileContent)
file1.close()
print(FileContent)
with open("example1.txt", "w") as file1:
    file1.write("Hey Guys, I've written this code !")
file1.closed
with open("example1.txt", "r") as filecopy:
    with open("example2.txt") as filewrite:
        for line in filecopy:
            filewrite.write(line)
    filewrite.close()
filecopy.close()
