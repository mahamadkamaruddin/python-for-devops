import re


text = "c,c++, python, java, rust, javascript, ruby, pascal, assembly, c#"
splitChar = ","
splitList = re.split(splitChar, text)

print("The spillted list: ", splitList)