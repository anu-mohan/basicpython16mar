import Numberword

print("__name__ value for this file: ", __name__)
print("__name__ value for numberword: ", Numberword.__name__)

usrInput = input("Enter any number:")
Numberword.printNumberToWord(int(usrInput))