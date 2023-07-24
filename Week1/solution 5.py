#Write a python script to enter any string and count vowel

# Function to count vowel
def vowel_count(str):
    count = 0
    vowel = set("omdhivar")
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
     
    print("No. of vowels :", count)
     
str = "omdhivar"
vowel_count(str)
