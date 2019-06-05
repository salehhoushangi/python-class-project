import random
chars="abcdefghijklmnopqrstuvwxyz"
number="0123456789"
symbols="@#$%&*+-=^"
password=''
username_list=[]
def simple_password(password):
    username_input=input("Enter username to create password to it:\n")
    lenght=int(input("Enter password lenght you want to create:\n"))
    for c in range(lenght):
        password += random.choice(chars+number+symbols+chars.upper())
   #print(password)
    print("your username: {} ".format(username_input))
    print("your passsword: {}".format(password))

def complex_passowrd(password):
    val2=''
    password_dict={"s":"$","a":"@","b":"Bb","c":"Cc","d":"Dd","f":"Ff","h":"Hh","e":"Ee","l":"Ll","p":"Pp","r":"Rr","y":"Yy","v":"Vv","i":"Ii","m":"Mm","o":"Oo"}
    username_input=input("Enter username to create password to it:\n")
    username_list=list(username_input)
    for c in range(len(username_list)):
        for key,value in password_dict.items():
            if username_list[c]== key:
                username_list[c]=str(value)
                val2 +=(username_list[c])
                password += random.choice(number+symbols+chars)

    print("your password is {}{}".format(val2,password))
            
while True:
    print("")
    password_menue=input('''Which method item number you want to create password .
    1.simple and wihtout remember format with optional lenght.
    2.strong and with remember format with system set lenght.
    3.Enter quit to Exit.\n\n ''').lower()
    if password_menue == "1":         
        simple_password(password)
    elif password_menue == "2":
        complex_passowrd(password)
    elif password_menue =="quit":
        break
    else :
        print("your item {} not recognized!.Please select 1 or 2 \n".format(password_menue))


