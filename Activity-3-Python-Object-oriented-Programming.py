# CC223-M: Applications Development and Emerging Technologies
# Activity 3: Python - Object oriented Programming
# Name: Ador, Angelo A. (olenieae - COLLABORATOR)
#       Hashim, Elizabeth Ann B. (eyyylizbth - COLLABORATOR)
#       Tolentino, Jesse Ann P.  (jesseanntolentino - OWNER)
# Section: BSIS - 2AB

import os

# It's a class that holds the user's character customization
class Customization:
    userCharacter = ""
    userWeapon = ""
    userAbility1 = ""
    userAbility2 = ""

    def __init__(self, character, weapon, ability1, ability2):
        """
        This function is used to create a new character object.
        
        :param character: The character the user chooses
        :param weapon: The weapon the user has chosen
        :param ability1: The first ability the user chooses
        :param ability2: The second ability the user chooses
        """
        self.userCharacter = character
        self.userWeapon = weapon
        self.userAbility1 = ability1
        self.userAbility2 = ability2

    def setCharCustomization(self):
        """
        It prints the user's character, weapon, and abilities
        """
        print("Character: " + self.userCharacter)
        print("Weapon: " + self.userWeapon)
        print("Ability 1: " + self.userAbility1)
        print("Ability 2: " + self.userAbility2 + "\n")

# It's a class that has a dictionary of characters and a method that returns the character chosen by
# the user
class Character:
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
        
        for key in self.characterList.keys():  # getting the menu_options.keys
            # display the menu_option
            print("[{}] {}".format(key, self.characterList[key]))

        while 1:
            option = int(input("Choose character: "))

            if option >= 1 and option <= 4:
                print("You have chosen " + self.characterList[option])
                return option, self.characterList[option]
            else:
                print("Invalid Input! Try again!")

# It's a class that prints out a list of weapons, and then asks the user to choose one.
class Weapon:
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

# It's a class that allows the user to choose two abilities from a list of four.
class Ability:
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
                            print("You have chosen " + self.abilityList.get(ch)[option1-1])
                            if option == option1:
                                print("Choose another skill! Try again!")
                            else:
                                return self.abilityList.get(ch)[option-1], self.abilityList.get(ch)[option1-1]
                    else:
                        print("Invalid Input! Try again!")
            else:
                print("Invalid Input! Try again!")

def header():
    print("\t\t=============================================")
    print("\t\t=---Welcome to Zenonia Warrior Customizer---=")
    print("\t\t=============================================")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    

# Main Function
PersonList = []
i = 0
os.system("cls")
header()
user = input("Please enter your Explorer Name: ")
os.system("cls")
header()
print("\"Welcome " + user.upper() + "!" + " I'm Olaf, your Warrior Assistant\"")
print("\"Please select \"two\" warriors and get themselves ready before having their journey to the magical world of Zenonia...\"\n")
while i < 2:
    print("Please Customize your Warrior No. " + str(i + 1))
    characterObject = Character()
    weaponObject = Weapon()
    abilityObject = Ability()
    
    ch = characterObject.getCharacter()   
    os.system("pause")
    os.system("cls")
    header()
    print("Please Choose Warrior " + str(i+1) + "'s Weapon")
    wp = weaponObject.getWeapon()
    os.system("pause")
    os.system("cls")
    header()
    print("Please Choose Warrior " + str(i+1) + "'s Ability")
    ab = abilityObject.getAbility(ch[0])
    os.system("pause")
    os.system("cls")
    header()
    PersonList.append(Customization(ch[1], wp, ab[0], ab[1]))
    i += 1

os.system("cls")
header()
print("\"Very Nice Choice " + user.upper() +"!\"")
print("\"Let us see your chosen warriors.\"\n")
warrior = 1

# It's a for loop that iterates through the PersonList and prints the user's character, weapon, and
# abilities.
for user in PersonList:
    print("Warrior No. " + str(warrior) + ":")
    user.setCharCustomization()
    warrior += 1

print("\"It's my pleasure to assist you\"")
print("\"Goodluck to your journey on the magical world of Zenonia!\"")