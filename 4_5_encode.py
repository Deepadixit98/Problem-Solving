"""Problem Statement
Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence. 

Rules are as follows: 
a. Spaces are to be retained as it is 
b. Each word should be encoded separately

If a word has only vowels then retain the word as is

If a word has a consonant (at least 1) then retain only those consonants

Note: Assume that the sentence would begin with a word and there will be only a single space between the words.

Sample Input                                    Expected Output

I love Python                                I lv Pythn

MSD says I love cricket and tennis too       MSD sys I lv crckt nd tnns t

I will not repeat mistakes                   I wll nt rpt mstks

 """

def sms_encoding(data):
    word=data.split()
    vowels="aeiouAEIOU"
    st=""
    for Letters in word:
        if(len(Letters)==1):
            st=st+Letters
        else:
            for j in Letters:
                if j not in set(vowels):
                    st=st+j
        st=st+" "
    return st[0:-1]

data="I want GOOD DAYS AND avoid BAD DAYS"
print(sms_encoding(data))


#  end