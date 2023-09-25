#we are going to 
import random

try: # We try to do thid step, but we skip if is an error
    import pyperclip 

except:
    pass


def main():
    user_text = input("Enter Your Message >")
    print()
    sponge_text = englishToSponge(user_text)
    print(sponge_text)

    try:
        pyperclip.copy(sponge_text)

    except:
       pass


def englishToSponge(text):
    '''Convert a message to Sponge meme Case '''
    sponge = ''
    useUpper = False

    for charchter in text:
        if not charchter.isalpha():
            sponge += charchter
            
        if useUpper:
            sponge += charchter.upper()
        else:
            sponge += charchter.lower()

        if random.randint(1, 100) <= 90:
            useUpper = not useUpper

    return sponge

if __name__ == "__main__":
    main()