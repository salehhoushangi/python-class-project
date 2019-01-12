shop_list = []
def help():
    print('''
  #####################################################################  
  ######### ******WELCOM TO ISIRAN STORE ***** ########################
  #########  Enter 'DONE' to stop adding items ########################
  #########  Enter 'HELP' to show all instructions in our app##########
  #########  Enter 'SHOW' to show all items in our shopping list#######
  ##################################################################### 
    ''')
help()
def  get_valu():
    item = input("> ").lower()
    return item
while True :
    item = get_valu()
    if item == "done":
        break
    elif item == "help":
        help()
    elif item == "":
        continue
    elif item == "show":
        print(shop_list)
    elif not item in shop_list:
            shop_list.append(item)
            print("Added {} to list now. your basket now has {} items".format(item,len(shop_list)))
    