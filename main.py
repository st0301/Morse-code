import re                                                  # imports the module to work with regular expressions, reference : https://docs.python.org/3/library/re.html
from character_29228875 import CharacterAnalyser as ch     # imports the CharacterAnalyser class  
from word_29228875 import WordAnalyser as wd               # imports the WordAnalyser class
from sentence_29228875 import SentenceAnalyser as se       # imports the SentenceAnalyser class
from decoder_29228875 import Decoder as de                 # imports the Decoder class
character=ch()
word=wd()
sentence=se()
decoder=de()

def main():
    finish=0                                    # new variable
    repeat=1                                    # new variable
    while repeat > finish:
        morse_code_sequence=''
        while True:
            enter = input("Type morse sequence. To terminate, type 'e'.\n")
            if len(enter)<1:                                                # at least one character
                enter = input("Type at least one character. To terminate, type 'e'.\n")
                morse_code_sequence+=decoder.decode(enter)+'\n'             # append to the morse_code_sequence
            elif len(enter)>1:
                morse_code_sequence+=decoder.decode(enter)+'\n'         # append to the morse_code_sequence
            if enter=='e':
                break
            
        print("Decoded outputs:\n",morse_code_sequence)
        
    
        process=input("The next choice:\n\
        Type 1 - character\n\
        Type 2 - word\n\
        Type 3 - sentence\n\
        Type 4 - all analysis\n\
        Your choice: ")                     # user chooses one of choice to see the result of process 
        
        if process==str(1):                                     # if a user type 1 then it calls the character analyser
            print("Decoded characters: ",first(morse_code_sequence))            
            print(character.__str__())
        
        elif process==str(2):                                   # if a user type 2 then it calls the word analyser
            print("Decoded words: ",second(morse_code_sequence))
            print(word.__str__())
        
        elif process==str(3):                                   # if a user type 3 then it calls the sentence analyser
            print(third(morse_code_sequence))
            print(sentence.__str__())
        
        elif process==str(4):                                   # if a user type 4 then it calls all analysis
            print("Decoded characters: ",first(morse_code_sequence))
            print(character.__str__())
            print("Decoded words: ",second(morse_code_sequence))
            print(word.__str__())
            print(third(morse_code_sequence))
            print(sentence.__str__())
        else:
            print("You type a wrong number")
            
        process=input("Type 1 to start again or type 2 to exit: ")          # if a user would like to continue or exit
        if process==str(1):                                                # if a user types 1 then the program continues the process 
            finish=0
            continue
        elif process==str(2):                                           # if a user types 2 then the program stops.
            finish+=1
            print("Exit from the program.")
            break
        else:                                                               # if a user types something different then 1 or 2, the program terminates.
            print("You type a wrong number. Exit from the program.")
            break

        
def first(morse_code_sequence):                                 # function called first to character analyser
    return(character.analyse_characters(morse_code_sequence))
def second(morse_code_sequence):                                # function called second to word analyser
    return(word.analyse_words(morse_code_sequence))
def third(morse_code_sequence):                                 # function called third to sentence analyser
    return("Number of sentences: "+str(sentence.analyse_sentences(morse_code_sequence)))

if __name__=='__main__':
    main()
