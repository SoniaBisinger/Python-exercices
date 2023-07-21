print("Replit Login System")

def login():
    username = input("What is your username?: ")
    password = input("What is your password?: ")
    if username == "david" and password == "baldies4life":
        print("Welcome to Replit!")
    else:
        print("Whoops! I don't recognize that username or password. Try again!")
        login()

login()
