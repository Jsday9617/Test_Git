prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

#using int() to accept Numerical Input
age = input("How old are you?")
#How old are you? 21
age = int(age) 

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride you're a little older.")

#study while loops, flags (breaks especially)