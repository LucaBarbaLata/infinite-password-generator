import string
from random import randint, choice




def generate_password3():
    password_min = 8
    password_max = 100
    all_chars = string.ascii_letters + string.digits
    password = "".join(choice(all_chars) for x in range (randint(password_min, password_max))) + "\n"
    with open("rockyou.txt", "a") as f:
        f.write(password)
        print("Password:")
        print(password)

        
        
        

while True: 
    generate_password3()