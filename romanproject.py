import math
from WorldTimeAPI import service

myclient = service.Client('timezone')
requests = {"area":"America","location":"New_York"}

# Returns a DateTimeJSON object
response = myclient.get(**requests)

timer = str(response.datetime).split('T')[1].split('.')[0]

print(timer)

Roman = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

while(True):
    value1 = input("Enter the first Roman numeral: ")
    if value1 not in Roman.keys():
        print("Try again")
    else:
        break
    
while(True):
    value2 = input("Enter the second Roman numeral: ")
    if value2 not in Roman.keys():
        print("Try again")
    else:
        break

def split(word):
    return [char for char in word]

list1 = split(value1)
list2 = split(value2)

sum1 = 0
sum2 = 0

#match each i to the value in the lists
#add the value to the sum
for i in list1:
    x = int(Roman[i])
    sum1 += x

for i in list2:
    y = int(Roman[i])
    sum2 += y

#Simply, prints the sum of both Roman inputs into numbers

if sum1 < sum2:
    print("The first Roman numeral is less than the second Roman numeral.")
    print("Roman to Number: " + str(sum2 - sum1))
else:
    print("The first Roman numeral is not less than the second Roman numeral.")
    print("Roman to Number: " + str(sum1 + sum2))

#Turns time into Roman numeral time (24h)
def integerToRoman(A):
    romansDict = \
        {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            5000: "G",
            10000: "H"
        }
  
    div = 1
    while A >= div:
        div *= 10
  
    div /= 10
  
    res = ""
  
    while A:
  
        # main significant digit extracted
        # into lastNum
        lastNum = int(A / div)
  
        if lastNum <= 3:
            res += (romansDict[div] * lastNum)
        elif lastNum == 4:
            res += (romansDict[div] +
                        romansDict[div * 5])
        elif 5 <= lastNum <= 8:
            res += (romansDict[div * 5] +
            (romansDict[div] * (lastNum - 5)))
        elif lastNum == 9:
            res += (romansDict[div] +
                        romansDict[div * 10])
  
        A = math.floor(A % div)
        div /= 10
          
    return res

def convert_timer(val):
    connect = ""
    for tim in val.split(':'):
        connect += str(integerToRoman(int(tim))) + ":"
    return connect

print(convert_timer(timer))