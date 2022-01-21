"""Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.

Rules:

1. The word should have the largest frequency.

2. In case multiple words have the same frequency, then choose the word that has the maximum length.

Assumptions:

1. The text has no special characters other than space.

2. The text would begin with a word and there will be only a single space between the words.

Perform case insensitive string comparisons wherever necessary."""

# def word_count(str):
#     counts = dict()
#     words = str.split()

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#     fre = max(counts)
    
#     return fre

# print( word_count('the quick brown fox jumps over the lazy dog.'))

# # str = "The Fox jumped on rock, rock got broken"
# # print(word_count(str))
# # end

def freq(str):
      
    str = str.split()         
    str2 = []

    for i in str:             
        if i not in str2:
            str2.append(i) 
              
    for i in range(0, len(str2)):
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))    
        # frequency = max(str.count(str2[i]))
        # print (frequency)    

     
def main():
    str ='apple mango apple orange orange apple guava mango mango'
    freq(str)                    
  
if __name__=="__main__":
    main()        