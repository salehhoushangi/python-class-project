import random

wrong_char =[]
my_list =[]
blank=[]
g=0
max_life=5
curren_life=0
random_index=random.randint(0,2)
letter_box=('apple','benana','orange','mango','strawberry','pumpkin')
target_letter=letter_box[random_index]
my_list= list(target_letter)
#print(my_list)

def print_blanks():
    global g
    print_blanks=len(my_list)
    for i in range(print_blanks):
        if g==0 : 
            blank.append('_')
    g+=1        
    print(' '.join(blank))    


def check_char():
    global curren_life
    if user_input in my_list:
        for b in range(len(my_list)):
            if user_input == my_list[b]:
                blank[b]=my_list[b]
    else:
        if not user_input in wrong_char:
            wrong_char.append(user_input)
        curren_life +=1

while True:
    print("")
    print("Can you guess what the fruit to be wrote?")
    print("Maximum wrong Answer {}/{}".format(curren_life,max_life ))
    print(', '.join(wrong_char))
    print("")
    print_blanks()
    user_input=input("enter your charecter:").lower()
    check_char()
    if not '_' in blank :
        print("your mission has been successfully accomplished")
        break
    if  curren_life==max_life:
        print("sorry you are Game over ")
        print("The right answer is (({}))".format(target_letter))
        break
