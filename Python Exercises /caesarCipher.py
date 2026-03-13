alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def caesarCipher(message = input("Type in your message taht should be encrypted "),p_key = input("Type your number that the message should ne encrypted by ")):
    p_key = int(p_key)
    encrypted_message = ""
    for letter in message:
        letter = letter.lower()
        if letter not in alphabet:
            encrypted_message += letter
            continue
        elif letter == "z":
            pos_in_alphabet = -1
            letter = alphabet[pos_in_alphabet+p_key]
            encrypted_message += letter
        else:
            pos_in_alphabet = alphabet.index(letter)
            letter = alphabet[pos_in_alphabet+p_key]
            encrypted_message += letter
    print(encrypted_message)
    return(encrypted_message)

caesarCipher()