from fileMethods import *
from curric import *
import time


fileName = 'courseData.txt'

while True:
    menu()
    choice = input(': ')
    if choice == '1':
        while True:
            print('\n\nCourse. (enter x to exit)')
            addString = input(": ")
            if addString == 'x':
                break
            newCourse = Course(addString)
            """
            Should check if the course already exists in the courseData
            file.
            """
            addToFile(fileName, newCourse.fileOut())
            clear()
    elif choice == '2':
        print('ARE YOU SURE? Type YES to confirm.')
        confirm = input(': ')
        if confirm == 'YESsldfkjsd':#make it hard to accidently erase
            eraseFile(fileName)
            time.sleep(1)
            clear()
        else:
            print('Returning to Menu...\n')
            time.sleep(1)
            clear()
    elif choice == '3':
        clear()
        printFile(fileName)
        noChoice = input("\nPush ENTER key to go on.")
        clear()
    elif choice == '0':
        break
