# continue / break

absent = [2, 5] #欠席
no_book = [7] #本がない
for student in range(1, 11) : #1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        print("{0}廊下に出て".format(student))
        break
    print("{0}, 本を読んで".format(student))

#------------------------------------------------------------------------

# for 

# 1，2，3，4の前に１００を付ける -> 101,102,103,104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 学生の名前を長さで変換
students = ["Iron man", "Thor", "groot"]
students = [len(i) for i in students]
print(students)

#学生の名前を大文字で変換
students = ["Iron man", "Thor", "groot"]
students = [i.upper() for i in students]
print(students)

