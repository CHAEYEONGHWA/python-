# if

weather = "good"
if weather == "rain":
    print("傘")
elif weather == "hot":
    print("サングラス")
else:
    print("X")

#weather = "今日の天気は"
#if weather == "rain":
#    print("傘")
#elif weather == "hot":
#    print("サングラス")
#else:
#    print("X")


weather = "rain" or weather == "snow"
if weather == "rain":
    print("傘")
elif weather == "hot":
    print("サングラス")
else:
    print("X")

#temp = int(input("気温はどうですか"))
#if 30 <= temp:
#    print("蒸し暑い")
#elif 10 <= temp and temp < 30:
#    print("いい")
#elif 0 <= temp < 10:
#    print("少し寒い")
#else:
#    print("注意")

#---------------------------------------------------------------------------

# for

#print("番号 : 1")
#print("番号 : 2")
#print("番号 : 3")
#print("番号 : 4")

for waiting_no in range(1,6):
    print("番号 : {0}".format(waiting_no))


stabucks = ["中村", "田中", "加藤"]
for customer in stabucks:
    print("{0}, お待たせしました".format(customer))

#----------------------------------------------------------------------------

#while

customer = "中村"
index = 5
while index >= 1:
    print("{0},お待たせしました. 残り {1} です。 ".format(customer, index))
    index -= 1
    if index == 0:
        print("捨てました")
    
#customer1 = "加藤"
#index = 1
#while True:
#    print("{0},お待たせしました。お呼び {1} ".format(customer1, index))
#    index += 1

customer_my = "佐藤"
person = "unknown"

while person != customer_my :
    print("{0}, お待たせしました。".format(customer_my))
    person = input("お名前お願いします")
 