#CS210
#
#PROJECT THREE
#
#PythonCode.py
#Jeremiah Blue
#
#Created on April 16th, 2022
#
#
#



import re
import string
import os.path
from os import path

#Description:
#       To call this function, pass the function name into the CallProcedure function.
#Example:
#       callProcedure("CountAll");
#Output:
#       Returns a list of all unique items in CS210, and prints all of their occurrances.
#Return:
#       None
def CountAll():
   #Open the file in read mode
   text = open("input.txt", "r")
   #Create an empty dictionary to store "found" words
   dictionary = dict()
   #Check each line of the input file
   for line in text:
       #remove any errant spaces and newline characters
       line = line.strip()
       #Convert characters to lowercase for better matching
       word = line.lower()
       
       #Check if the word is already in the dictionary
       if word in dictionary:
           #Increment number of times the word appears
           dictionary[word] = dictionary[word] + 1
       else:
           #If the word is not in the dictionary, add it w/ a value of 1
           dictionary[word] = 1
   #Print all contents of the dictionary
   for key in list (dictionary.keys()):
       print(key.capitalize(), ":", dictionary[key])
   #Close the opened file.
   text.close()

#Description:
#       To call this function, pass this function into the CallIntFunc function along with the desired search term.
#Example:
#       callIntFunc("CountInstances", searchTerm);
#Output:
#       Returns the number of occurrances of the desired search term.
#Return:
#       int wordCount
def CountInstances(searchTerm):
   #Convert user-inputted search term to lowercase for better matching
   searchTerm = searchTerm.lower()
   #Open the file in read mode
   text = open("input.txt", "r")
   #Create variable to track how many times the search term has been "found"
   wordCount = 0
   #Check each line of the input file
   for line in text:
       #remove any errant spaces and newline characters
       line = line.strip()
       #Convert characters to lowercase for better matching
       word = line.lower()
       
       #Check if the found word is equal to the user's input
       if word == searchTerm:
           #Increment number of times the word appears
           wordCount += 1
   #Return the number of times the search term was found, as per specification
   return wordCount
   #Close opened file
   text.close()

#Count the number of appearances for each item, then write to frequency.dat
#Description:
#       To call this function, pass this function into the CallProcedure function.
#Example:
#       callProcedure("CollectData");
#Output:
#       Returns a a document (frequency.dat) with each unique word and the number of times that word occurs..
#Return:
#       frequency.dat
def CollectData():
   #Open the input file in read mode
   text = open("input.txt", "r")
   #Create and/or write the file frequency.dat
   frequency = open("frequency.dat", "w")
   #Create an empty dictionary to store "found" words
   dictionary = dict()
   #Check each line of the input file
   for line in text:
       #remove any errant spaces and newline characters
       line = line.strip()
       #Convert characters to lowercase for better matching
       word = line.lower()
       
       #Check if the word is already in the dictionary
       if word in dictionary:
           #Increment number of times the word appears
           dictionary[word] = dictionary[word] + 1
       else:
           #If the word is not in the dictionary, add it w/ a value of 1
           dictionary[word] = 1
   #Write each key and value pair to frequency.dat
   for key in list (dictionary.keys()):
       #Format the key-value pair as strings followed by a newline.
       frequency.write(str(key.capitalize()) + " " + str(dictionary[key]) + "\n")
   #Close the opened files
   text.close()
   frequency.close()