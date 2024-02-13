import re
string="Simple is better than complex. Complex is better than complicated."
# pattern=re.compile(r'is')
# obj=pattern.match(string)
# obj=pattern.search(string)
# print (obj.start(), obj.end())

# obj=pattern.findall(string)
# print (obj)

# obj=pattern.sub(r'was', string)
# print (obj)


pattern = re.compile(r"is")
iterator = pattern.finditer(string)
print(iterator)

for match in iterator:
    print(match.span())


import re
text = "He was carefully disguised but captured Quickly by police."
obj = re.findall(r"\w+ly\b", text)
print (obj)

text = "Error shoulb never pass silently. Unless explicitly silenced."
obj = re.findall(r"\b[aeiouAEIOU]\w+", text)
print(obj)


