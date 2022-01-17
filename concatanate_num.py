"""Problem Statement
Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. 
Note: Assume that all the numbers are two digit numbers.
 

Sample Input      Expected Output

23,34,55n           553423

"""

def create_largest_number(number_list):
    number_list.sort()
    res = ""
    for num in number_list:
        res = str(num) + res

    return (int(res))


number_list = [87, 66, 11]
largest_number = create_largest_number(number_list)
print(largest_number)

# end