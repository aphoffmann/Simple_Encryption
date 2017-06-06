# CS1210 HW2
# Alex Hoffmann


from random import randint
from itertools import permutations, islice

######################################################################
# Some utility functions.

# Returns the ith permutation of input sequence S (as a list).
def getPerm(S, i):
    return(next(islice(permutations(S), i, None), None))
    

# Computes n!
def factorial(n):
    if n == 0:
        return(1)
    result = 1
    for i in range(1, n+1):
        result = result * i
    return(result)

# Generates a random key between 0 and n!
def genKey(n):
    return(randint(1, factorial(n)) - 1)

######################################################################
# A test sentence.
S = "It’s a beautiful day in the neighborhood"

######################################################################

def isVowel(c): 
    '''Checks if c is a vowel'''
    if c.lower() in ('a', 'e', 'i', 'o', 'u', ' '):
        return(True)
    else:
        return(False)
    

def chunk(S): 
    '''Splits S into chunks and maps the beginning and ending indices
       with if-statements by iterating through each index, 0-len(S)'''
    #initializing variabes
    listOfIndices = [0]
    index = 0
    
    #Loop cycles through string S to collect start and end indices of each syllable into a list 
    while index < len(S):
        if index + 1 == len(S): #last iteration and last index
            listOfIndices.append(index+1)
            index += 1
            
        elif isVowel(S[index]) == isVowel(S[index+1]): #increments index if both are consonant or vowel
            index += 1
            
        elif isVowel(S[index+1]) == False: #increments index if the next letter is a consonant
            index += 1
            
        else:
            listOfIndices.append(index+1) #appends index to list because a vowel is following a non-vowel
            index += 1
    chunks = [(listOfIndices[x], listOfIndices[x+1]) for x in range(len(listOfIndices)-1)]
    return chunks

def encode(S, i):
    '''Finds number of possible permutations and reorders string S into permutation i of that list'''
    S = ' ' + S + '.'
    newForm = list(getPerm(chunk(S), i)) # gets unordered list of chunks
    x = 0 #indexer
    list1 = [] 
    while x < len(newForm): # creates list of strings from the indices in the unordered list.
        a = newForm[x][0]
        b = newForm[x][1] 
        list1.append(S[a:b])
        x += 1
        
    return ''.join(list1) #returns combined strings

def invertChunk(c, i):
    '''takes encrypted S and back tracks transposition of indices based on perm/key i'''
    indices = range(len(chunk(c))) #create list of indices length chunk
    indices = list(getPerm(indices, i)) #Get perm using key and reorder indices according to permutation
    
    #Zip with newChunks, using indices as markers
    #sorted([newChunks, key=lambda x: x[0]) Source: http://bit.ly/2cI2GPY
    #create new list of sorted chunks with [x[1] for x in myList]
    enumChunks = [x[1] for x in sorted([i for i in zip(indices, chunk(c))], key=lambda x: x[0])]
    return enumChunks   

def decode(S, i):
    '''unencrypts S with key i. Assembles the string the same was as encode()'''
    oldForm = invertChunk(S, i)
    x = 0
    list1 = []
    while x < len(oldForm): #creates list of strings from the indices in oldForm.
        a = oldForm[x][0]
        b = oldForm[x][1]
        list1.append(S[a:b])
        x += 1
    return ''.join(list1)[1:-1] #creates string by joining list of strings

if (__name__ == '__main__'):
    key = genKey(len(chunk(S)))
    print(S)
    E = encode(S, key)
    D = decode(E, key)
    print(E)
    print(D)





