"""Problem Statement
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 

Assume that the sentence would begin with a word and there will be only a single space between the words.

Perform case sensitive string operations wherever necessary.

Sample Input                              Expected Output

the sun rises in the east               eht snu sesir ni eht stea

 """

vowels=['a','e','i','o','u']

def encrypt_sentence(sentence):
    final=[]
    list_sentence = sentence.split(" ")
    for index,word in enumerate(list_sentence):
        if (index+1)%2!=0:
            final.append(word[::-1])
        else:
            v=[]#to store all vowels
            t=[]#to store the letters temporily
            for letter in word:
                if letter not in vowels:
                    t.append(letter)
                else:
                    v.append(letter)
            t.extend(v)
            final.append("".join(t))
    #if len(final)>1:
    return " ".join(final)
                    
# sentence="the"
# encrypted_sentence=encrypt_sentence(sentence)
# print(encrypted_sentence)
sentence="The Sun sets in the west."
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)

# end