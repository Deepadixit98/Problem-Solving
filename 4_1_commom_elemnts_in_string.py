"""Problem Statement
Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

Sample Input                                       Expected output

"I like Python"
"Java is a very popular language"                       lieyon

"""

 
def find_common_characters(msg1,msg2):
    list=[]
    for i in msg1:
        if i==" ":
            continue
        else:
            for j in msg2:
                if i == " ":
                    continue
                elif i == j:
                    if i in list:
                        break
                    else:
                        list.append(i)
                        break
    output="".join(list)
    if len(output)==0:
        return -1
    else:
        return output
#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)

# end