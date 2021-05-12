import re

def problemD():
    with open('samples/samples-D/3.in.txt') as file:
        inputs = file.readlines()
        for i in inputs:
            print(i)
            location = i.find("exam")
            if location != -1:
                if re.search("[a-zA-Z]", i[location + 3:]):
                    return("O.O")
        return("ZzZ")

print(problemD())