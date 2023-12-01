def decaler_caractere(caractere, decalage):
    code_ascii = ord(caractere)
    nouveau_code_ascii = code_ascii - decalage  #if "+" its the code in level09 
    nouveau_caractere = chr(nouveau_code_ascii)
    return nouveau_caractere



file_path = './token'
file_contents = ""
try:
    with open(file_path, 'r', encoding='ISO-8859-1') as file: #not working utf-8 
        file_contents = file.read()
        print(file_contents)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

#original = "abcd" #test
original = file_contents[:-1]
new = ""
i = 0
for letter in original:
    #print("letter :",letter)
    new += decaler_caractere(letter, i)
    i += 1

print(f"original : {original}")
print(f"new : {new}")