import random
i=0
b=0
my_list =[]
blank=[]
random_index=random.randint(0,2)
letter_box=('apple','benana','orange')
target_letter=letter_box[random_index]
my_list= list(target_letter)
my_list =[ch for ch in target_letter]
print(my_list)

def print_blanks():
    global i
    print_blanks=len(my_list)
    for i in range(print_blanks):
        blank.append('_')
        print(blank[i],end=" ")
        
    #print (blank)


def check_char():
    global b
    indexes = [b for b in range(len(my_list)) if my_list[b] == user_input]
    for b in range(len(my_list)):
        if user_input == my_list[b]:
            print (my_list[indexes[b]],end="")
            #m = my_list.index(my_list[b])
            #print(next(m),next(m))
    print(indexes)
            
            



print_blanks()
print("")
user_input=input("enter your charecter:")
check_char()




