# 🔹 Task 1: Encrypt and Decrypt a File
# 🔹 Write a Python program that:

# Asks the user for a filename and a shift key (integer).
# Reads the content of the file and encrypts it using Caesar Cipher (shift each character by the key value).
# Saves the encrypted text in "encrypted.txt".
# Writes another function to decrypt the encrypted file and store the original content in "decrypted.txt".

def encryptWord(word:str,shift:int):
    encryptText = ""
    for i in range(len(word)):
        character = word[i]
        #for uppercase
        if character.isupper():
            encryptText += chr((ord(character) + shift-65) % 26 + 65)
        else:
            encryptText += chr((ord(character) + shift-97) % 26 + 97)
    return encryptText

def decryptWord(word:str,shift:int):
    decryptText = ""
    for i in range(len(word)):
        character = word[i]
        #for uppercase
        if character.isupper():
            decryptText += chr((ord(character) - shift-65) % 26 + 65)
        else:
            decryptText += chr((ord(character) - shift-97) % 26 + 97)
    return decryptText


text = input("Enter a Word : ")
shift = int(input("Enter the Shift : "))
if not text or not shift>=0:
    print("Please Enter the shift and Word")
else:
    encrytResult = encryptWord(text,shift)
    decryptResult = decryptWord(encrytResult,shift)
    print("Original :",text)
    print("Shift :",shift)
    encryptFile = open("encrypted.txt","w")
    decryptFile = open("decrypted.txt","w")
    encryptFile.write(encrytResult)
    decryptFile.write(decryptResult)
    encryptFile.close()
    decryptFile.close()
    readEncrypt = open("encrypted.txt","r")
    readDecrypt = open("decrypted.txt","r")
    print("Encrypted:", readEncrypt.read())
    print("Decrypted: ",readDecrypt.read())
    readEncrypt.close()
    readDecrypt.close()