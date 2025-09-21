# 1. for istifadə edərək 1-dən 100-ə qədər bütün cüt ədədlərin cəmini tap.

"""
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
"""

# 2. while ilə 1-dən 50-yə qədər bütün ədədləri ekrana yazdır.

"""
count = 0

while count != 50:
    count+=1
    print(count)
"""

# 3. Verilmiş siyahıda ([2, 7, 3, 9, 12, 15, 8]) yalnız cüt ədədləri seçib yeni siyahıya yığ (for).

"""
list = [2, 7, 3, 9, 12, 15, 8]
new_list = []

for i in list:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)
"""

# 4. İstifadəçidən bir söz al və onu for ilə tərsinə çevir.

"""
enter = input("Enter a word >>> ").lower()

reversed_word = ""

for i in enter:
    reversed_word = i + reversed_word 

print(f"Reversed word:{reversed_word}")
"""

# 5. [1, 2, 3, 4, 5] siyahısından cüt və tək ədədləri ayrı siyahılara böl (for).

"""
list = [1, 2, 3, 4, 5]
even = []
dot = []

for i in list:
    if i % 2 == 0:
        even.append(i)
    else:
        dot.append(i)
print(f"Dot is {dot} and even numbers is {even}")
"""

# 6. İstifadəçidən daxil edilən ədədin faktorialını hesabla (for).

"""
enter = int(input("Enter number for get number's factorial >>> "))

def factorial(o):
    a = 1
    for i in range(1, o+1):
        a *= i

    print(f"Finnal number is {a}")


factorial(enter)
"""

# 7. while ilə istifadəçidən rəqəmlər daxil edilməsini istəyin. 0 daxil ediləndə dayansın, daxil edilənlərin cəmini hesabla.

"""
count = 0

while True:
    enter = int(input("Enter number for get plused and if want stop write 0 >>> "))
    if enter == 0:
        break
    else:
        count += enter
print(count)
"""

# 8. Verilmiş siyahının ([10, 20, 30, 40]) elementlərini while ilə çap et.

"""
list = [10, 20, 30, 40]
count = 0

while count != len(list):
    print(list[count])
    count += 1
"""

# 9. İstifadəçidən şifrə istəyin. Şifrə "ce23usaqlari" olana qədər təkrar soruşsun (while).

"""
while True:
    enter = input("Enter your password >>> ").lower()
    if enter == "ce23usaqlari":
        print("Password is correct")
        break
    else:
        print()
        print("Password incorrect")
        print()
"""

# 10. Verilmiş ədədin rəqəmlərinin sayını while ilə tap.

"""
enter = int(input("Enter number >>> "))
count = 0

while enter > 0:
    enter = enter // 10  
    count += 1 
print(count)
"""

# 11. while ilə verilmiş ədədin rəqəmlərinin cəmini tap.

"""
enter = int(input("Enter number like 123 -> 6 >>> "))
finnal = 0
count = 0
enter_str = str(enter)

while count != len(enter_str):
    finnal += int(enter_str[count])
    count += 1  

print(f"Final number is {finnal}")
"""

# 12. Verilmiş stringdən (məs: "hello world") hər hərfin neçə dəfə istifadə olunduğunu say və dict şəklində çıxart (for).

"""
text = "hello world"
count = {}

for i in text:
    if i != " ": 
        if i in count:
            count[i] += 1 
        else:
            count[i] = 1 
print(count)
"""

# 13. while ilə istifadəçi mənfi ədəd daxil edənədək davam etsin, daxil edilən ən böyük müsbət ədəd tapılsın.

"""
list = []

while True:
    enter = int(input("Enter number for stop write negative number >>> "))
    if enter < 0:
        if len(list) == 0:
            print("You not writed any thing")
        else:
            print(max(list))
        break
    else:
        list.append(enter)
"""

# 14. while ilə istifadəçidən sözlər daxil et, exit yazana qədər davam et, sonunda bütün sözləri çap et.

"""
txt = " "

while True:
    enter = input("Enter text for stop write exit >>> ")
    if enter.lower() == "exit":
        print(txt)
        break
    else:
        txt += f"{enter} \n"
"""

# 15. [1,2,3,4,5,6,7,8,9] siyahısındakı bütün mümkün ədədlər cütlərinin hasilini çıxart və yeni siyahıya əlavə et (for).

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list = []


for i in range(len(numbers)):
    for x in range(i+1, len(numbers)): 
        a = numbers[i] * numbers[x] 
        list.append(a)

print(list)
"""

# 16. Verilmiş siyahıda təkrarlanan elementləri çıxarıb yalnız unikal elementlərdən ibarət siyahı düzəlt (for).

"""
list = [1, 2, 3, 1, 4, 2, 5, 6, 3]
dupe = []

for i in list:
    if list.count(i) > 1 and i not in dupe:
        dupe.append(i)

print(f"Not duplicate numbers: {list}")
print(f"Duplicate numbers: {dupe}")
"""
