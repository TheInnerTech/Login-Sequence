import time
Username = "InternTech"
Password = "83318"
Wait = 1

Username_Input = input("\nEnter Username: ")
if Username_Input == Username:
    Password_Input = input("Enter Password: ")
    if Password_Input == Password:
        for Wait in range(3):
            print(".")
            time.sleep(1.5)
            Wait += Wait
        print("\nThankyou, " + "Sign-In Successfully" + "!\n")
        print("." + time.sleep(5))
        
    
    else:
        print("\nTry Again, " + "Password Invailid" + ".\n")
else:
    print("Try Again, " + "Password Invailid" + ".\n")


