print(" Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).\n")

firstnum = int(input("Enter First Number: "))
secnum = int(input("Enter Second Number: "))
sign = input("Enter compute sign ")

if sign == "+":

    answer = int(firstnum + secnum)
    print(firstnum,  "", sign, "", secnum, "=", answer)

elif sign == "-":

    answer = int(firstnum - secnum)
    print(firstnum,  "", sign, "", secnum, "=", answer)

elif sign == "/":

    answer = int(firstnum / secnum)
    print(firstnum,  "", sign, "", secnum, "=", answer)

elif sign == "*" or sign == "x":
    answer = int(firstnum * secnum)
    print(firstnum,  "", sign, "", secnum, "=", answer)
else:
    print("error")


