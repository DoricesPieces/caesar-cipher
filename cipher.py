# Caesar Cipher assignment
message = input("Please enter a sentence:")
shift = 5
result = ""
#Go through each letter in the message
for l in message.upper():
    #Only change letters not punctuation not spaces
    if l.isalpha():
        #Assigns number to letter from ASCII
        letter_key = ord(l)
        encypted_letter = letter_key + shift
        #Z is 90 on ASCII but other character follow
        if encypted_letter > 90:
            encypted_letter -= 26
            #convert back to corresponding letter
        encrypted_sentence = chr(encypted_letter)
        result = result + encrypted_sentence
    else:
        result += l
print(result)