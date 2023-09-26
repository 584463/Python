letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"


letter_list = letters.split()



def decode(secret_phrase):
    for key in range(26):
        for i in range(len(secret_phrase)):
             
            if secret_phrase[i] in letter_list:
                index = letter_list.index(secret_phrase[i])
                coded_index = (index + key) % 26
                print(letter_list[coded_index], end="")
            
            else:
                print(secret_phrase[i], end="")
        print()

decode("NEZEWGVMTX")