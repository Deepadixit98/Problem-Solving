"""Problem Statement
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program

Sample Input       Expected Output

AAAABBBBCCCCCCCC     4A4B8C

AABCCA               2A1B2C1A """

def encode(message):
    output=''
    privious=message[0]
    i=1
    count=1
    while len(message)>i:
        if privious==message[i]:
            count+=1
        else:
            output+=str(count)+privious
            count=1
            privious=message[i]

        if i==len(message)-1:
            output += str(count) + privious
        i+=1
    if len(message)==1:
        output += str(count) + privious
    return output

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)

# end
