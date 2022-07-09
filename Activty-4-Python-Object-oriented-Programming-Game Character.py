# CC223-M: Applications Development and Emerging Technologies
# Activity 3: Python - Object oriented Programming
# Name: Ador, Angelo A. (olenieae - COLLABORATOR)
#       Hashim, Elizabeth Ann B. (eyyylizbth - COLLABORATOR)
#       Tolentino, Jesse Ann P.  (jesseanntolentino - OWNER)
# Section: BSIS - 2AB

# Importing the necessary libraries for the program to run.
from email.header import Header
import os
import abc
import csv


# CustomizationInterface is an abstract class that defines the interface for the Customization class
class CustomizationInterface(abc.ABC):
    @abc.abstractclassmethod
    def __init__(self):
        pass

    def setCharCustomization(self):
        pass

    def StoreData(self):
        pass

    def PrintCSV(self):
        pass


# The CharacterInterface class is an abstract class that defines the getCharacter method
class CharacterInterface(abc.ABC):
    @abc.abstractclassmethod
    def getCharacter(self):
        pass


# This class is an abstract class that has an abstract method called getWeapon()
class WeaponInterface(abc.ABC):
    @abc.abstractclassmethod
    def getWeapon(self):
        pass


# <code>AbilityInterface</code> is an abstract class that defines the <code>getAbility</code> method
class AbilityInterface(abc.ABC):
    @abc.abstractclassmethod
    def getAbility(self):
        pass


# This class is used to create a new character object
class Customization(CustomizationInterface):
    arr = []
    getuserName = ""
    userCharacter = ""
    userWeapon = ""
    userAbility1 = ""
    userAbility2 = ""   
    def __init__(self, userName = "", character = "", weapon = "", ability1 = "", ability2 = ""):
        """
        This function is used to create a new character object.

        :param character: The character the user chooses
        :param weapon: The weapon the user has chosen
        :param ability1: The first ability the user chooses
        :param ability2: The second ability the user chooses
        """
        self.getuserName = userName
        self.userCharacter = character
        self.userWeapon = weapon
        self.userAbility1 = ability1
        self.userAbility2 = ability2

    def setCharCustomization(self):
        """
        It prints the user's character, weapon, and abilities
        """
        """
        It prints the user's character, weapon, and abilities
        """
        print("Character: " + self.userCharacter)
        print("Weapon: " + self.userWeapon)
        print("Ability 1: " + self.userAbility1)
        print("Ability 2: " + self.userAbility2 + "\n")
    
    def getUsername(self):
        """
        The function is supposed to check if the username is already taken, if it is, it will return to
        the main menu, if not, it will proceed to the next function
        :return: The username
        """
        valid = 1
        found = 0 
        with open('Customization.csv', 'a', encoding='utf-8', newline = '') as empty_file:
            empty_file.close()
        file = 'Customization.csv'
        if os.stat(file).st_size == 0:
            header()
            self.getuserName = input("Please enter your Explorer Name: ")
            os.system("cls")
            header()
            print("\"Welcome " + self.getuserName.upper() + "!" +" I'm Olaf, your Warrior Assistant\"")
            print("\"Please select a warrior and get themselves ready before having their journey to the magical world of Zenonia...\"\n")
            return self.getuserName.upper()
        else:
            while valid == 1:
                header()
                
                self.getuserName = input("Please enter your Explorer Name: ")
                with open('Customization.csv') as csv_file:
                    read_characters = csv.reader(csv_file, delimiter = ',')
                    for row in read_characters:
                
                        if row[0].upper() == self.getuserName.upper():
                            found = 1
                            break
                if found == 1:
                    print("\n\nUsername Taken, Please Try Again! Returning Main Menu")
                    valid == 1
                    os.system("pause")
                    os.system("cls")
                    MainMenu()   
                else:
                    csv_file.close()
                    os.system("cls")
                    header()
                    print("\"Welcome " + self.getuserName.upper() + "!" +" I'm Olaf, your Warrior Assistant\"")
                    print("\"Please select a warrior and get themselves ready before having their journey to the magical world of Zenonia...\"\n")
                    return self.getuserName.upper()

    def StoreData(self):
        """
        It takes the user's input and stores it in an array.
        """
        info_arr = [self.getuserName, self.userCharacter, self.userWeapon, self.userAbility1, self.userAbility2]
        self.arr.append(info_arr)

    def PrintCSV(self):
        """
        It opens a file called Customization.csv, appends to it, and writes the contents of the array arr
        to it.
        """
        with open('Customization.csv', 'a', encoding='utf-8', newline = '') as empty_file:
            writer = csv.writer(empty_file)
            for row in self.arr:
                writer.writerow([i for i in row])


# The Character class is a class that implements the CharacterInterface class
class Character(CharacterInterface):
    characterList = {
        1: 'Wizard',
        2: 'Knight',
        3: 'Archer',
        4: 'Assasin',
    }

    def getCharacter(self):
        
        """
        It prints the menu options, then asks the user to choose a character, then prints the character
        they chose, then returns the option and the character they chose
        :return: The option and the characterList[option]
        """

        for key in self.characterList.keys():  
           
            print("[{}] {}".format(key, self.characterList[key]))

        while 1:
            option = input("Choose character: ")

            if len(option) == 0:
                print("Input is Empty! Try again!")
            elif int(option) >= 1 and int(option) <= 4:
                print("You have chosen " + self.characterList[int(option)])
                return option, self.characterList[int(option)]
            else:
                print("Invalid Input! Try again!")




# The class Weapon is a child class of WeaponInterface. It has a dictionary called weaponList
class Weapon(WeaponInterface):
    weaponList = {
        1: 'Wizard Staff',
        2: 'Sword',
        3: 'Bow & Arrow',
        4: 'Katar',
    }

    def getWeapon(self):
      
        """
        It prints out a list of weapons, then asks the user to choose one, and returns the weapon they
        chose.
        :return: The weapon that the user has chosen.
        """
        for key in self.weaponList.keys():
            print("[{}] {}".format(key, self.weaponList[key]))
        while 1:
            option = int(input("Enter weapon: "))

            if option >= 1 and option <= 4:
                print("You have chosen " + self.weaponList[option])
                return self.weaponList[option]
            else:
                print("Invalid Input! Try again!")


# The class Ability is a subclass of AbilityInterface. It has a class variable called abilityList
# which is a dictionary with four keys, each of which has a list of four strings as its value
class Ability(AbilityInterface):
    abilityList = {
        1: ["Energy Ball", "Dragons Breath", "Crown of Flame", "Hail Storm"],
        2: ["Fire Slash", "Power Slash", "Gigantic Storm", "Chaotic Disaster"],
        3: ["Take Aim", "Quick Shot", "Blazing Arrow", "Frost Arrow"],
        4: ["Cloaking", "Enchant Posion", "Sonic Acceleration", "Meteor Assault"],
    }

    def getAbility(self, ch):
        """
        The function takes in a character as a parameter and returns two abilities from a list of four

        :param ch: character
        :return: the two abilities that the user has chosen.
        """
        j = 1

        for i in self.abilityList.get(ch):
            print("[{}] {}".format(j, i))
            j += 1

        while 1:
            option = int(input("Enter Ability 1: "))
            if option >= 1 and option <= 4:
                while 1:
                    print("You have chosen " + self.abilityList.get(ch)[option-1])
                    option1 = int(input("Enter Ability 2: "))
                    if option1 >= 1 and option1 <= 4:
                        print("You have chosen " +
                              self.abilityList.get(ch)[option1-1])
                        if option == option1:
                            print("Choose another skill! Try again!")
                        else:
                            return self.abilityList.get(ch)[option-1], self.abilityList.get(ch)[option1-1]
                    else:
                        print("Invalid Input! Try again!")
            else:
                print("Invalid Input! Try again!")


def header():
    """
    This function prints out a header for the program.
    """
    print("\t\t=============================================")
    print("\t\t=---Welcome to Zenonia Warrior Customizer---=")
    print("\t\t=============================================")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")


# Main Function
def MainMenu():
    PersonList = []
    obj = Customization()
    i = 0
    os.system("cls")
    getUserObject = Customization()
    username = getUserObject.getUsername()
    print("Please Customize your Warrior")
    characterObject = Character()
    weaponObject = Weapon()
    abilityObject = Ability()

    ch = characterObject.getCharacter()
    os.system("pause")
    os.system("cls")
    header()
    print("Please Choose your Warrior's Weapon")
    wp = weaponObject.getWeapon()
    os.system("pause")
    os.system("cls")
    header()
    print("Please Choose Warrior's Ability")
    ab = abilityObject.getAbility(int (ch[0]))

    os.system("pause")
    os.system("cls")
    PersonList.append(Customization(username, ch[1], wp, ab[0], ab[1]))
    header()


    os.system("cls")
    header()
    print("\"Very Nice Choice " + username + "!\"")
    print("\"Let us see your warrior setup.\"\n")

    for user in PersonList:
        user.setCharCustomization()
        user.StoreData()

    obj.PrintCSV()

    print("\"It's my pleasure to assist you\"")
    print("\"Goodluck to your journey on the magical world of Zenonia!\"")
    os.system("pause")
    MainMenu()

MainMenu()