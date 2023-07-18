#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui


person = Person(0, 0)
#Create instance of main social network object
ai_social_network = SocialNetwork()
ai_social_network.add_current_user(person)

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()
            

        elif choice == "2":
            username = input("What's your username? ") 
            current_user = ai_social_network.add_current_user(username)
            inner_menu_choice = social_network_ui.manageAccountMenu()
            # Handle inner menu here
            while True:
                if inner_menu_choice == "1":
                    print("Change username")
                    ai_social_network.current_user.name = input("Write your new username: ")
                    ai_social_network.current_user.age = input("Write your new age: ")
                    break

                elif inner_menu_choice == "2":
                    #print("the name is: ", ai_social_network.current_user.name)
                    #print("the name ois age: ", ai_social_network.current_user.age)
                    addedfriend = input("What is your friends name?  ")
                    current_user.add_friend(addedfriend)
                    # ai_social_network.current_user.
                    break
                
                elif inner_menu_choice == "3":
                    current_user.view_friends()
                    break

                elif inner_menu_choice == "4":
                    friend_name = input ("Enter the name of the person you want to contact: ")
                    friend = ai_social_network.add_current_user(friend_name)
                    current_user.send_message(friend)
                    
                elif inner_menu_choice == "8":
                    current_user.view_messages()
                    

                elif inner_menu_choice == "5":
                    break
                elif inner_menu_choice == "6":
                    username = input("Who would you like to block? ")
                    current_user.block_friend(username)
                    break
                elif inner_menu_choice == "7":
                    current_user.view_blocklist()
                    break
    
                inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
