
def is_int(choice):
    try:
        int(choice)
        return True
    except ValueError:
        return False

def choice_validation(choice,menu_or_dif):
    while is_int(choice) != True:
        print("Sorry invalid choice.")
        choice = input("1: To play game\n2: To exit\n")
    if menu_or_dif == "menu":
        choice =  int(choice)
       #print("#2",choice)
        if choice != 1 and choice !=  2 :
            #if choice != 2:
            print("Sorry invalid choice.")
            choice = input("1: To play game\n2: To exit\n")
            #print("#3",choice)
            choice_validation(choice,"menu")

            #else:
            #    return int(choice)
        return int(choice)
    if menu_or_dif == "dif":
        choice =  int(choice)
        print("#2",choice)
        if choice != 1 and choice != 2 and choice !=  3 :
            #if choice != 2:
            print("Sorry invalid choice.")
            choice = input("1: To play game\n2: To exit\n")
            print("#3",choice)
            choice_validation(choice,"dif")

        return int(choice)
'''
def choice_validation(choice):
    l = choice
    print("#2",choice,l)
    if choice == "1" or choice == "2":
        return choice
    elif choice != "1" and choice != "2":
        print("#3",choice,l)
        print("Sorry invalid choice.")
        choice = input("1: To play game\n2: To exit\n") 
        print("#4",choice,l)
        choice_validation(choice)
    print(choice)
    return choice

    print("hellow")
'''    

    
'''    
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")    
choice = input("1: To play game\n2: To exit")
l = choice_validation(choice,"menu")

print(l,type(l))
#print(choice_validation(choice),type(choice_validation(choice)))
#if l != 1 and l!= 2:
#    l = choice_validation(choice,'menu')
'''