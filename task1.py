# ------- میانگین محاسبه----
li = [1, 20, 18, 11, 1, 19, 15, 17, 16, 10, 5, 8, 8, 20, 18, 19, 10, 1, 15, 15]
avg = sum(li) / len(li)
print(avg)
#  حذف تکرار ها از لیست
li1 = set(li)
print("list after removing duplicate element:", li1)
# بزرگترین و کوچکترین عدد لیست
my_list_minimum = min(li)
my_list_maximum = max(li)
print('my list minimum;', my_list_minimum)
print('my list maximum;', my_list_maximum)
# معکوس کردن رشته ها
string = 'abcdedifg'
reversed_chars = reversed(string)
reversed_string = ''.join(reversed_chars)
print(reversed_string)
# split string
string1 = 'hello word;my name is tina...'
print(string1.split())
# تبدیل اعداد صحیح به رشته
print(str(int(input('Enter your number to convert number to text:'))))
# برعکس کردن رشته2
string2 = str(input("Enter your string for reversed: "))
print(string2[::-1])
# تعداد تکرار یک کاراکتر در یک رشته
string3 = str(input("Enter your string: "))
Count = str(input("Enter your letters: "))
print(f'{Count} repeat in{string3}:', string3.count(Count))
# تبدیل رشته به حروف کوچک و بزرگ
string4 = str(input("Enter your string: "))
print(f'convert {string4} to lowercase letter:', string4.lower())
print(f'convert {string4} to lowercase uppercase:', string4.upper())
# اولین تکرار در متن
string4 = str(input("Enter your string to find the first iteration: "))
Find = str(input("Enter your letters: "))
print(f'{Find} repeat in place {string4.find(Find)}')

