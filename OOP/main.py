# Character Class Assignment by Sami

# Task 1

class character:
    def __init__(self, name, cphrase1, cphrase2):
        self.name = name
        self.cphrase1 = cphrase1
        self.cphrase2 = cphrase2
        self.level = 0

# Methods

    def speak(self, phraseNum):
        if phraseNum == 1:
                 print(self.cphrase1)
        elif phraseNum == 2:
                 print(self.cphrase2)

    def setLevel(self, newLevel):
          self.level = newLevel
          print(newLevel)

# Task 2

character1 = character("Kung Fu Panda", "Skadoosh", "You have been blinded by pure awesomeness")
character2 = character("Spiderman", "My Spider-Sense is tingling", "Your friendly neighbourhood spiderman.")

# Task 3

character1.speak(1)
character2.setLevel(2)
character2.speak(2)
