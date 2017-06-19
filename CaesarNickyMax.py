#Provide 3 options, Encrypt, Decrypt or Quit
#if the user chooses encrypt:
    #ask for phrase to encrypt
    #ask for key to encrypt it with
    #store inputted message as a string
    #store key as an integer
    #convert to lowercase 
    #convert lowercase to unicode numbers
    #add the key amount to the unicode numbers ensuring the code 
    #doesn't convert any special characters by using if statements limiting the 
    #code to the lowercase alphabet
    #convert the new unicode to lowercase letters
    #iterate and store in a new list
    #print that list
#if user chooses decrypt:
    #ask for phrase to decrypt 
    #ask for key to decript with
    #store phrase as a string
    #store key as an integer
    #convert to lowercase
    #convert lowercase to unicode numbers
    #minus the key amount to the unicode numbers ensuring the code 
    #doesn't convert any special characters by using if statements limiting the 
    #code to the lowercase alphabet
    #convert the new unicode to lowercase letters
    #iterate and store in a new list
    #print that list
#if answer is quit
#end program
    
done = False

def encrypt():
    encryption = ""
    enc = input("Insert the phrase you'd like to encrypt:")
    key = int(input("Insert your key or shift:"))
    enc = enc.lower()
    for char in enc:
        x = ord(char)
        if x >= 97:
            x += key
            while x > 122:
                x = (x - 122 + 96)
        x = chr (x)
        encryption += x
    print (encryption)

def decrypt():
    dec = input("What phrase would you like to decrypt?: ")
    key2 = int(input("What key or shift would you like to use?: "))  
    dec = dec.lower()
    decryption = ""
    for char in dec:
        x = ord(char)
        if x >= 97:
            x -= key2
            while x < 97:
                x = (x - 97 + 123)
        x = chr (x)
        decryption += x
    print (decryption)        

while not done:
    print ("Welcome to the Encryption Machine.")
    print ("Please select an option from the list below.")
    print ("A. Encrypt.")
    print ("B. Decrypt.")
    print ("Q. Quit.")
    begin = input(": ")
    
    if begin.lower() == "a":
        encrypt() 
        
    elif begin.lower() == "b":
        decrypt()   
    
    elif begin.lower() == "q":
        done = True