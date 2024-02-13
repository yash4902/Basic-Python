from string import Template

TemStr = Template("Hello $name")
newStr = TemStr.substitute(name = "Yash")
print(newStr)

dct = {"name":"abc"}
newStr = TemStr.safe_substitute(dct)
print(newStr)


