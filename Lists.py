list1 = [10, 20, "Aayan", 15]
x = 10
print(list1[0])
print(list1[2])
print(list1[0:2])
for i in list1:
    print(i)
list2 = [1,2,3,4,5,6,7,8,9,10]
total = 0
for i in list2:
    total += i
print(total)
def match(words):
    count1 = 0
    list3 = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            count1 += 1
            list3.append(word)
    print("List of words with first and last letters same: ", list3)
list4 = ["1221", "abc", "qqqq", "yes", "bob"]
count2 = match(list4)
print("Words that are being matched: ", list4)
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
print("All even numbers: ", even)
#average
sum = 0
for i in numbers:
    sum += i
len = 0
for j in numbers:
    len += 1
average = sum / len
print("Sum: ", sum)
print("Length:", len)
print("Average:", average)
def maxfinder(list):
    maxnum = list[0]
    for num in list:
        if num > maxnum:
            maxnum = num
    return maxnum
def minfinder(list):
    minnum = list[0]
    for num in list:
        if num < minnum:
            minnum = num
    return minnum
max1 = maxfinder(numbers)
max2 = maxfinder([15,23,45,67,1,26,89])
print(max1)
print(max2)
min1 = minfinder(numbers)
min2 = minfinder([15,23,45,67,1,26,89])
print(min1)
print(min2)
merge = [max1, max2, min1, min2]
print(merge)