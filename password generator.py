import  random

lower = "abcdefghijklmnopqrstuwxyz"
upper = lower.upper()
symbols = "!@#$%^&*()_+[]{};:'\|'/?,.<>"
numbers = "1234567890"
all = lower + upper +symbols + numbers

length = int(input('set lenght of password: '))

password = ''
for _ in range(length):
    password = "".join({password, random.choice(all)})

print(password)
