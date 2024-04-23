# age = 56
# price = 19.91
# fi = "name"
# lol = False
# print(age)

# var = input("This is a input: ")
# print("Hello" + var)

# year = input("Year: ")
# age = 2020 - int(year)
# print(age)

# #PRAC1
# sting = "this is a small but good paragraph about Sam somoneer"
# sting = sting.lower()
# for i in sting.split():
#     if i.startswith('s'):
#         print(i)

# #Prac2
# str = "Python is a programming language"
# str1 = list(str.split())
# print(str)
# print(str1)
# for i in str1:
#     if len(i)%2 == 0:
#         print(i)

# #Prac3
# for i in range(1,100):
#     if( i%3==0 and i%5==0):
#         print("FIZZBUZZ")
#     elif(i%3==0):
#         print("FIZZ")
#     elif(i%5==0):
#         print("BUZZ")
#     else:
#         print(i)

# #Prac7
# str = "This is a Revolution and We arent going to Stop!"
# upper = 0
# lower = 0
# for i in str:
#     if i.isupper():
#         upper+=1
#     elif i.islower():
#         lower += 1
# print(upper)
# print(lower)

# ls = [1,4,4,5,2,2,44,12,1,2,44,52,4]

# def purify(ls):
#     lt = [];
#     for i in ls:
#         if i not in lt:
#             lt.append(i)
#         else:
#             print(lt)

# purify(ls)

# def print_square():
#     while True:
#         try:
#             num = int(input("Enter an integer: "))
#             square = num * num
#         except ValueError:
#             print("Please enter a valid integer.")
#         else:
#             print(f"The square of {num} is: {square}")
#             break

# print_square()

# import datetime

# today = datetime.date.today()
# print(f"Today is: {today}")

# for i in range(1,6):
#     nextd = today + datetime.timedelta(days=i)
#     print(f"Day{i}:{nextd}")

# def ghaai():
#     py = 10
#     def pr(py):
#         print(py)
# ghaai
# p = 25
# if p > 25 and p < 30:
#     print(p)
# else:
#     print(ghaai().pr(10))

ls = ["1", "2", "3"]
y = [1,2,3]
thisobj = {
    "key" : "value",
    "no." : 97,
    "val" : True
}

var = dict.fromkeys(y, ls)  
print(var)

