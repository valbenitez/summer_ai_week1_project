# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                            # you can save objects of people on the network in this list
        
    ## For more challenge try this

    def add_current_user(self, current_user):
        for person in self.list_of_people:
            if person.id == current_user:
                return person

    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here
        print("Creating ...")
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        user = Person(name, age)
        self.list_of_people.append(user)
        return user
    
    def send_message(person,message):
        #implement sending message to friend here
        pass
    

    
        



class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.blocklist = []
        self.messages = []

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        self.friendlist.append(person_object)
        print(self.friendlist)
       

    def view_friends(self):
        print(self.friendlist)

    def view_messages(self):
        print(self.messages)

    def block_friend(self, person_object):
        self.blocklist.append(person_object)
        

    def view_blocklist(self):
        print("Current blocked users:")
        print(self.blocklist)

    def send_message(self, person_object):
        message = input("Enter your message: ")
        person_object.messages.append(message)
        print("Message sent!")

