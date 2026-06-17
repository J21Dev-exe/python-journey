# Question 9:
''' 
Take BMI value and categorize:
<18.5      Underweight
18.5-24.9  Normal
25-29.9    Overweight
30+        Obese
'''

#===================================
# Solution:
print('9.')

# Print category acc to BMI
weight = float(input('Enter weight(in kg): '))      # weight in kg
height = float(input('Enter height(in m): '))       # height in m

BMI = ((weight)/(height * 2))                       # BMI calculate

print(BMI)

if (BMI < 18.5):                                    # if condition - underweight
    print('Individual is Underweight')
elif (BMI < 24.9):                                  # elif 1st condition - Normal
    print('Individual is Normal')
elif (BMI < 29.9):                                  # elif 2nd condition - Overweight
    print('Individual is Overweight')
else:                                               # else condition - Obese
    print('Individual is Obese')
#===================================