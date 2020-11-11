import re

file1 = open("1.txt", "r")

for line in file1:
    if (re.findall(r'8\d\d\d-\d\d\d-\d\d-\d\d\n', line) or re.findall(r'8[(]\d\d\d[)]\d\d\d-\d\d-\d\d\n', line)) \
            or ((re.findall(r'\d\d\d\d\d\d\d\d\d\d\d\n', line)) and (line[0] == "8")
                or (line[0] == "7")) \
            or (re.findall(r'9\d\d\d\d\d\d\d\d\d\n', line)):
        print(line)
file1.close()
