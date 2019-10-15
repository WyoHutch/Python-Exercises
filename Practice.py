import random
import math
from functools import reduce

#Function to reverse a string
# arr = "word"
# print(arr[::-1])

#Function to reverse a sentence
# sent = "This is a cat"
# def reverse_sent(sent):
    # words = sent.rsplit(" ")
    # newsent = ""
    # for i in range(len(words)):
    #     newsent = newsent + words[len(words) - i - 1] + " "
    # print(newsent)

#Function to list words in a sentence vertically between symbols
# sent = "This is a cat really"
# def list_words(sent):
    # words = sent.rsplit()
    # # print(12*"#")
    # for word in words:
    #     # print("#  " + word + (8-len(word))*" "+"#")
    # print(12*"#")

# Function to return randon hexadecimal color
# color = int(random.random() * 0x1000000)
# print(color, format(color, '#6x'))

#Function to return whether a number is even or odd
# def is_even(x):
#     if x % 2 == 0:
#         print(str(x) + " is even.")
#     else:
#         print(str(x) + " is not even.")

# is_even(16)

# Function to return middle number (median) in a list
# arr = [1, 5, 6, 8, 2, 4, 9, 8, 3]
# arr.sort()
# print(arr[int(len(arr) / 2 - 0.5)])

# Function to return a value based on string input of mathematical function
# def operation(x, y, oper):
#     d = ("'" + str(x) + " " + oper + " " + str(y) + "'")
#     print(d)
#     # print(eval(d))
#     if oper == "+": return x + y
#     if oper == "-": return x - y
#     if oper == "*": return x * y
#     if oper == "/": return x / y
#     if oper == "^": return x ** y

# print(operation(3, 4, "+"))

# Function (#1) to return list ed values of a number
# x = 125489637
# def numlist1(x)
    # arr = []
    # while x >= 1:
    #     arr.insert(0, x % 10)
    #     x = int(x/10)
    # print(arr)

# Function (#2) to return list ed values of a number
# x = 125489637
# def numlist2(x):
    # res = [int(num) for num in str(x)]
    # print(res)

# Function to loop until number is correctly guessed
# num = 7
# guess = 0
# while guess != num
#     guess = int(input("Enter a number guess"))
# print("Your guess : " + str(guess) + " is correct")

# Function to check that a string is a palindrome or not
# def palinchecker(palindrome):
#     palindromelc = palindrome.lower()   # lower case palindrome
#     pal_list = []       # initial list of string characters
#     for i in range(len(palindromelc)) :
#         if palindromelc[i] != " " and palindromelc[i] != "," :  # remove spaces and commas
#             pal_list.append(palindromelc[i])
#     pal_rev_list = pal_list[::-1]
#     if reduce(lambda x,y: x + y, pal_list) == reduce(lambda x,y: x + y, pal_rev_list) :
#         trustr = ""
#     else :
#         trustr = "not "
#     print("'" + palindrome + "' is " + trustr + "a palindrome")

# pdrome = "A man, a plan, a canal, panama"
# palinchecker(pdrome)

#Function to remove first and last values in a list
# my_arr = [1, "a", 1, "b", 2, "d", 5, 6, "h", "r", 7]
# def removefl(my_arr):
#     my_arr.pop()
#     my_arr.pop(0)
#     print(my_arr)

# Program to convert a list of items into one string
# my_list1 = ["a", "b", "c", "d", "e"]
# print(reduce(lambda x,y: x + y, my_list1))

# Program to print every third item in a list starting with the third
# my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(my_list2[2::3])

# Program to multiply all items in a list to one product
# my_list3 = [1, 2, 3, 4]
# print(reduce(lambda x,y: x * y, my_list3))

# Program to find the most frequent item in a list
import operator
my_list4 = [3, "a", "a", "b", 2, 3, "a", 3, "a", 2, 4, 9, 3, 3]
my_list4.sort(key = str)
modecnt = 1     # greatest count 
modeval = ""    # greatest count item
itemdict = {}   # list item : count
itemval = ""
valcnt = 1
for i in range(len(my_list4)) :
# for item in my_list4 :
    if not isinstance(my_list4[i], str) :
        itemstr = str(my_list4[i])
    else :
        itemstr = my_list4[i]
    if itemstr == itemval :
        valcnt += 1
    else :
        if i != 0 :     # skip first item add to dictionary
            itemdict[itemval] = valcnt
        if valcnt > modecnt :   # new mode item and count
            modeval = itemval
            modecnt = valcnt
        valcnt = 1      # reinitialize counter
        itemval = itemstr
itemdict[itemstr] = valcnt
if valcnt > modecnt :   # test last item for mode
    modeval = itemval
    modecnt = valcnt
print("mode is : '" + modeval + "' - (" + str(modecnt) + " times)")
print(itemdict)
dict_val_sort = sorted(itemdict.items(), key = operator.itemgetter(1), reverse = True)
# print(dict_val_sort)
print(dict_val_sort[0:])    # list of dictionary elements, value: count

# Function to return incrementing square matrices
def manual_incrementing_matrix(size):                # Matrix size
    mat_list = []               # Initialize zero matrix
    for i in range(size):   # Loop thru the rows
        mat_row = []            # Initialize zero matrix row
        j = i                   # Initialize first row element
        for k in range(size):   # Loop thru the column values
            mat_row.append(j)
            j += 3
        # print(mat_row, ",")
        mat_list.append(mat_row)    # append row to matrix
    return mat_list

manual_incrementing_matrix(10)

mat_list2 = [[0 for i in range(5)] * 5]
# print(mat_list2)

def incr_matrix(size):
    mat_list3 = [[i + j for i in range(size)] for j in range(size)]
    return mat_list3

print(incr_matrix(5))
