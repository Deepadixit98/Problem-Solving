getwd()
#ctrl enter
10+5
10.43
'deepa'
"Deepa"
"9"
T
F
1


#variable 
x <- 21
x

a = 45.6
a
A = 55
A

class(A)   #the function that shows data type of the value 
class(a)

 B= 100L  # writing L at the end makes it  understand 
         #machine that it is integer value 

 class(B) 
 class(a) #no function is give to specify float value
 
 
 
#character 
 
C <- "We are learning R "
C
class(C)

#boolea/ logical

D = T
E = F
D
E

class(D)
class(E)


sum = a+A 
sum

#Data structures  = to store more than one data values 
#two types of data structures  = 1.homogeneous and 2.hetrogeneous
#1.homogeneous = stores same type of data types
#ex. : Vector (1 dimension)
#2.hetrogeneous = stores differrent/dissimilar type of data types
#ex. : 1.list (1 dimension) 
#   & 2.Dataframes(2 dimension) - has rows and columns i.e Table


#Vector
marks <- c(85, 98, 54, 35, 29)
marks

Names <- c("Deepa", "Sharvil", "Pllavi", "Saurabh", "Aman")
class(Names)

info <- c("d", 3.6, 8, T)


#Accessing elements from vector

info[1]
info[4]
info[1,2]
info[1:2]  #specifying range
info[2:4]
info[c(1,4)]





