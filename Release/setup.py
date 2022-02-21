import re
import string

def ListItemsPurchased():
    frequency = {}
    with open('GroceryList.txt') as file:
        # Finds the frequency of each word in the text file 
        lines = file.read().split()
        for word in lines:
            count = frequency.get(word,0)
            frequency[word] = count + 1
        # Allows us to see our keys 
        frequency_list = frequency.keys()
        # Gets the items and their frequency
        for words in frequency_list:
            print (words, frequency[words])
    file.close()
    
    return None

def FrequencyOfItem(item):
    frequency = {}
    item_frequency = 0
    with open('GroceryList.txt') as file:
        # Finds the frequency of each word in the text file 
        lines = file.read().split()
        for word in lines:
            count = frequency.get(word,0)
            frequency[word] = count + 1
        # Allows us to see our keys 
        frequency_list = frequency.keys()
        # Gets frequency of item
        for words in frequency_list:
            if words == item:
                item_frequency = frequency[words]
    file.close()

    return item_frequency

def ItemHistogram():
    frequency = {}
    with open('GroceryList.txt') as file:
        # Finds the frequency of each word in the text file 
        lines = file.read().split()
        for word in lines:
            count = frequency.get(word,0)
            frequency[word] = count + 1
        # Allows us to see our keys 
        frequency_list = frequency.keys()
        # Creates a new file if it does not exist
        file = open('frequency.dat', 'w')
        for words in frequency_list:
            # Writes to new file and places items and frequency next to each other
            file.write('{0} {1}\n'.format(words, str(frequency[words])))
        # Makes new file readable
        with open(r"frequency.dat") as file:
            for data in file:
                print(data.split()[0], end=' ')
                item_frequency = int(data.split()[1])            
                print('*' * item_frequency)
    file.close()

    return None