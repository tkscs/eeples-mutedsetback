song = "I like to eat, eat, eat, apples and bananas"



def sing(vowel):
    new_sentence = ""
    
    for character in song:
        if character in "aeiou":
            new_sentence = new_sentence + vowel
        elif character in "AEIOU":
            new_sentence = new_sentence + character
        else:
            new_sentence = new_sentence + character
        
    print(new_sentence)
    
   
sing("ay")
sing("ee")
sing("i")
sing("o")
sing("u")