def greet_user():
    print("Hello!, user")
    
# greet_user()

# def aoa(name):
#     print(f"Assalam-o-Alaikum, {name}!")
    
# aoa("Farooq")

# def aoa(name="Khuda k banday"):
#     print(f"Assalam-o-Alaikum, {name}!")
    
# aoa("Farooq")

#return values

# def square(number):
#     return number * number
# print(square(5))


# def fictorial(n):
#     if n==1:
#         return 1
#     else:
#         return n * fictorial(n-1)

# print(fictorial(5))

x=lambda a: a*2
print(x(5))
x=lambda a,b:a*b
print(x(4,5))