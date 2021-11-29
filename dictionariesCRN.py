# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 00:09:38 2021
@author: Richard Paglia


"""

totalClasses = {}

allClasses = [{'CRN': '35407', 'Desc': 'ECON 101: Principles of Macroeconomics'},
{'CRN': '30770', 'Desc': 'HIST 101: Western Civilization'},
{'CRN': '37573', 'Desc': 'MATH 140: Precalculus'}]


def classDeletion():
    classToDelete = input('Class to delete: ')
    for element in allClasses:
        if classToDelete in element['CRN']:
            result = next(item for item in allClasses if item['CRN'] == classToDelete)
            print(f'\033[0;43;mDeleting the class {result} from the class list!!\n\033[0;0;m')
            allClasses.remove(result)
            return
            
    print(f'\033[0;31;mNo Course {classToDelete} classes taken.\033[0;0;m')

def addClass():
    #Need to add error correction to this block!!
    classCRN = input('Enter the CRN of the course to be added: ')
    classDesc = input('Enter a description of the course to be added: ')
    classInfo={'CRN':classCRN,'Desc':classDesc}
    totalClasses = classInfo
    allClasses.append(totalClasses)
    return allClasses 
 
def menu():
    while True:
        print ("\n\n\nClass Dictionary Menu")
        print ("\033[0;36;m----------------------\033[0;0;m")
        print ("1) Display Classes Taken")
        print ("2) Add Class to Dictionary")
        print ("3) Remove Class from Dictionary")    
        print ("Q) Exit\n")
        choice = input('Enter your choice: ').lower()
        
        if choice == '1':
            if allClasses:
                allClassesSorted = sorted(allClasses , key = lambda i: (i['CRN'], i['Desc']))
                print('\n\nClasses Taken')
                print("\033[0;36;m--------------\033[0;0;m")
                print(*allClassesSorted, sep = '\n' )
            else:
                print("\n\033[0;31;mNo classes taken...\033[0;0;m")
                input('Press Enter to return to menu...')
        elif choice == '2':
            addClass()
        elif choice == '3':
            classDeletion()
        elif choice == 'q':
            return
        else:
            print(f'\033[0;31;mNot a correct choice: <{choice}>,try again\033[0;0;m')
 
if __name__ == '__main__':
    menu()    
    


