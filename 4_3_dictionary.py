"""Problem Statement
Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
1. CORRECT, if it is an exact match.
2. ALMOST CORRECT, if no more than 2 letters are wrong
3. WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
Assume that the words contain only uppercase letters and the maximum word length is 10.

Sample Input :                                                                        

{"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}


Expected Output :

[2, 2, 1]

 """
def find_correct(word_dict):
    condition1,condition2,condition3,count_of_wrong_letter=0,0,0,0
    for values in word_dict:
        if(word_dict[values]==values):
            condition1=condition1+1
        elif(len(word_dict[values])!=len(values)):
            condition3=condition3+1
        else:
            x=word_dict[values]
            for i in range(len(x)):
                if(x[i]!=values[i]):
                    count_of_wrong_letter=count_of_wrong_letter+1
            if(count_of_wrong_letter<=2):
                condition2+=1
            else:
                condition3+=1
            count_of_wrong_letter=0
    list=[condition1,condition2,condition3]
    return list
        
                
word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))

#  end