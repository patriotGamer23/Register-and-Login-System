import os.path
import hashlib

user_data = {}
attempts = 0

if os.path.exists("users.txt"):
    f = open("users.txt", "r")
    for line in f:
        words = line.split(" ")
        name = words[0]
        info = (words[1], words[2], words[3])
        user_data[name] = info
    f.close()
f = open("users.txt", "a+")

def check_username(l_name):
    if not(user_data.get(l_name)):
        print("This username does not exist!")
        return False
    else:
        return True

def hash_password(password):
    b = bytes(password, 'utf-8')
    return hashlib.sha256(b).hexdigest()

    
startup_message = input("Enter c for create accout or enter l for login. q to quit ")

while (startup_message == "c" or startup_message == "l" and startup_message != "q") and attempts < 5:
    if startup_message == "c":
        name = input("Username: ")
        tpassword = input("Password: ")
        password = hash_password(tpassword.strip('\n'))
        birthday = input("Birthday: ")
        secret = input("Secret: ")
        info = (password, birthday, secret)
        r = str(name + " " + password + " " + birthday + " " + secret + "\n")
        user_data[name] = info
        print(user_data[name])
        f.write(r)
    elif startup_message == "l":
        l_name = input("Username: ")
        check = check_username(l_name)
        if check == False:
            attempts += 1
            print("You have done " + str(attempts) + (" attemps out of the five attempt max"))
            continue
        l_password = input("Password: ")
        l_password = hash_password(l_password.strip('\n'))
        info = user_data[l_name]
        if l_password == info[0]:
            print(info)
        else:
            attempts += 1
    startup_message = input("Enter c for create accout or enter l for login. q to quit ")

f.close()


