alphabet = " !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]_abcdefghijklmnopqrstuvwxyz{|}~"
key = "qwertyuioplkjhgfdsazxcvbnm{|}~!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ [\]_"

def encrypt(message):
    result = ""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result
    
def decrypt(message):
    result = ""

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result


unencrypted_message = "BLACK panther IS going to be so good ~ riqht?([I know I am)]"
encrypted_message = encrypt(unencrypted_message)
decrypt_message = decrypt(encrypted_message)
    
print(unencrypted_message)
print(encrypted_message)
print(decrypt_message)
