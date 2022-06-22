code = {

    0: 52037,
    6: 52081,
    5: 52063,
    1: 52077,
    9: 52077,
    10: 52080,
    4: 52046,
    3: 52066,
    8: 52085,
    7: 52081,
    2: 52077,
    11: 52066,

}

password = ""

for i in range (max(code.keys()) + 1):
	password += chr(code[i] - 0xCafe)

print (password)