'''
Objective :- A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”.
'''

# Takes the Text as user input
info = input('Paste the text here: \t') 

# Checks the Text
check_1 = info.count('subscribe' or 'Subscribe' or 'SUBSCRIBE')
check_2 = info.count ('buy now' or 'Buy Now' or 'BUY')
check_3 = info.count('click this' or 'CLICK' or 'Click This')
check_4 = info.count('make' and 'money' or 'MONEY' or 'Make' and 'Money')

# Gives Output after analysing
if (check_1 != 0):
    print('It\'s a Spam')
elif (check_2 != 0):
    print('It\'s a Spam')
elif (check_3 != 0):
    print('It\'s a Spam')
elif (check_4 != 0):
     print('It\'s a Spam')
else :
    print('Not a spam')