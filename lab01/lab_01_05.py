# Lab01_05 - Exercise 1
print("h")
print("he")
print("hel")
print("hell")
print("hello")
print("hello w")
print("hello wo")
print("hello wor")
print("hello worl")
print("hello world")

print("using loop")
my_str = "My name is acm"
for i in range(len(my_str)):
	if my_str[i] == " ":
		continue
	print(my_str[:i+1])