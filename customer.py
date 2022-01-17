# # class Customer:
# #     def __init__(self):
# #         cust_id = 100

# # c1=Customer()
# # print(c1.cust_id)
# # class Customer:
# #     def __init__(self):
# #         self.id = 100

# # c1=Customer()
# # print(c1.id)
# class Customer:
#     def __init__(self,id1):
#         self.id = id1

# c1=Customer(200)
# print(c1.id1)

class Table:                         #Line1
    def __init__(self):              #Line2
        self.no_of_legs=4            #Line3
        self.glass_top=None          #Line4
        self.wooden_top=None         #Line5
    def identify_rate(self):         #Line6
        if(self.glass_top==True):    #Line7
            rate=20000               #Line8
        elif(self.wooden_top==True): #Line9
            rate=30000               #Line10
        else:                        #Line11
            rate=0                   #Line12
        return rate                  #Line13
dining_table=Table()                 #Line14
glass_top=True