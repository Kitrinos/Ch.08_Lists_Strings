#Sign your name:________________

'''
1.)
Write a single program that takes any of the three lists, and prints the average. 
Use the len function. There is a sum function I haven't told you about. 
Don't use that. Sum the numbers individually as shown in the chapter. 
Also, a common mistake is to calculate the average each time through the loop 
to add the numbers. Finish adding the numbers before you divide.
# '''
# a_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]
# b_list = [4,15,2,7,8,3,1,10,9]
# c_list = [5,10,13,12,5,9,2,6,1,8,8,9,11,13,14,8,2,2,6,3,9,8,10]
#
# list_total = 0
#
# for item in a_list:
#     list_total += item/len(a_list)
# print(list_total)
#
# for item in b_list:
#     list_total += item/len(b_list)
# print(list_total)
#
# for item in c_list:
#     list_total += item/len(c_list)
# print(list_total)

'''
2.) Write a program that will strip the username (whatever is in front of the @ symbol)
from any e-mail address and print it. First ask the user for their e-mail address.
'''
# email = input("Hi, Please input your email here : ")
#
# print(email[0:email.find("@")])

'''
TEXT FORMATTING:
3.) Make following program output the following:
     
     Score:          41,237
     High score:  1,023,407
     
     Do not use any plus sign (+) in your code.
     You should only have two double quotes in each print statement.
     '''
# score = 41237
# highscore = 1023407
# print("Score:      " + "{:,}".format(score))
# print("High score: " + "{:,}".format(highscore) )




