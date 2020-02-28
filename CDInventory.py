#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignment 05 utilizing dictionary to add, load, save, delete, and display inventory 
# Change Log: (Who, When, What)
# DBiesinger, 2020-Jan-01, Created File
# JRios, 2020-Feb-22, File Modified to load dictionary data
# JRios, 2020-Feb-24, File Modified to add listing data, deleting data
# JRios, 2020-Feb-27, File Modified, loading and deleting function edited
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Album': data[1], 'Artist': data[2]}
            lstTbl.append(dicRow)
            
        objFile.close()
        
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        lstRow = [intID, strTitle, strArtist]
        lstTbl.append(lstRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row, sep = ', ')
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        print('ID\tTitle by Artist \n')
        for row in lstTbl:
            print('{}\t{} by {}'.format(*row.values()))
        intID - int(input('Select ID to delete: '))
        for i in range(len(lstTbl)):
            if lstTbl[i]['ID'] == intID:
                del lstTbl[i]
                break
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row:
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

