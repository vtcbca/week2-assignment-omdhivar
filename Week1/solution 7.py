#Write a python script to enter any string, replace vowel with its position number

def replaceVowelsWithK(test_str, d):
 
    # string of vowels
    vowels = 'omdhivar'
 
    # iterating to check vowels in string
    for ele in vowels:
 
        # replacing vowel with the specified character
        test_str = test_str.replace(ele, d)
 
    return test_str
 
# input string
input_str = "om dhivar"
 
# specified character
d = "#"
 
print("Given String:", input_str)
print("Given Specified Character:", d)
print("After replacing vowels with the specified character:",
      replaceVowelsWithK(input_str, d))
