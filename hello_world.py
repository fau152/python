line = "------------------------------------------\n"

# 第一章 起步
message = "hello python world!"
print(message)

# 第二章 字符串
print(line)
str = "thIs iS ChinA"
str1 = str.title()
print(str.title())
print(str1)
print(str.upper())
print(str.lower())

print(line)
first_name = "wang"
last_name = "long"
full_name1 = f"{first_name.title()}{last_name.title()}"
print("full_name1: " + full_name1)
full_name2 = "{}{}".format(first_name.title(),last_name.title())
print("full_name2: " + full_name2)

print(line)
str2 = "  python  "
print(str2.rstrip())
print(str2.lstrip())
print(str2.strip())

# 第二章 数
print(line)
print(3**2)
print(0.1+0.2)
print(4/2)
print(0.1**(-2)+10)
num = 22_222.2_222
print(num)

print(line)
x,y,z = 1,2,3
print(f"{x}\t{y}\t{z}")

print(line)
NUM = 500
print(NUM)
NUM = NUM + 1
print(NUM)

# 第二章 注释
print(line)
'''
print("hello注释")
'''
print("hello")
