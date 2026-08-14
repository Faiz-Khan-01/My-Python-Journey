'''
Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.
'''
# Takes the Student's Marks as input
marks_1 = float(input('Enter your marks(in %) of first subject:\t'))
marks_2 = float(input('\nEnter your marks(in %) of second subject:\t'))
marks_3 = float(input('\nEnter your marks(in %) of third subject:\t'))

# Analyses the marks
total_marks = marks_1 + marks_2 + marks_3
check_1 = marks_1 >= 33
check_2 = marks_2 >= 33
check_3 = marks_3 >= 33
final_check = check_1 and check_2 and check_3 

# Gives the Output
if (total_marks >= 40 and final_check is True):
    print('You\'re passed')
else :
    print('You\'re failed')