#list

subway1 = 10
subway2 = 20
subway3 = 30
# ->
subway = [10,20,30]
print(subway)

subway = ["田中", "佐藤", "伊藤"]
print(subway)

#伊藤さんは何番目の電車に乗っていますか
print(subway.index("伊藤"))

#加藤さんが次の駅で次の車両に乗る
subway.append("加藤")
print(subway)

#中村さんを田中さんと伊藤さんの間に乗せる
subway.insert(1, "中村")
print(subway)

#後ろから一人ずつ降りる
print(subway.pop())
print(subway)

#同じ名前を持っている人は何人
subway.append("田中")
print(subway)
print(subway.count("田中"))

#整列も可能
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#逆も可能
num_list.reverse()
print(num_list)

#全部消す
num_list.clear()
print(num_list)

#様々な形と一緒に使える
mix_list = ["田中", 30, True]
print(mix_list)

#拡張
num_list = [5,2,4,3,1]
num_list.extend(mix_list)
print(num_list)

#---------------------------------------------------------------------------

#Dictionary
cabinet = {3:"田中", 100:"伊藤"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) -> error
#print(cabinet.get(5)) -> none
print(cabinet.get(5,"使える"))

print(3 in cabinet) #True or False

my_cabinet = {"A-3":"田中", "B-3":"伊藤"}
print(my_cabinet["A-3"])
print(my_cabinet["B-3"])

#新しいお客さん
print(my_cabinet)
my_cabinet["C-3"] = "加藤"
print(my_cabinet)

#変更
my_cabinet["A-3"] = "中村"
print(my_cabinet)

#帰ったお客さん
del my_cabinet["A-3"]
print(my_cabinet)

#keyだけ
print(my_cabinet.keys())

#valauだけ
print(my_cabinet.values())

#key, value
print(my_cabinet.items())

#closed
my_cabinet.clear()
print(my_cabinet)

#--------------------------------------------------------------------------

#Tuple

menu = ("とんかつ", "串カツ")
print(menu[0])
print(menu[1])

#menu.add("カツ丼") #追加できない

name = "田中"
age = 20
hobby = "soccer"
print(name, age, hobby)

(name, age, hobby) = ("田中", "20", "soccer")
print(name, age, hobby)

#--------------------------------------------------------------------------

#set -> 重複できない、順番ない

my_set = {1,2,3,3,3}
print(my_set) # 重複できない

java = {"田中", "伊藤", "中村"}
python = set(["田中", "佐藤"])

#重なる名前
print(java & python)
print(java.intersection(python))

#合わせて
print(java | python)
print(java.union(python))

#javaはできるが、pythonはできない人
print(java - python)
print(java.difference(python))

#pythonができる人が増える
python.add("伊藤")
print(python)

#javaができなくなった人
java.remove("伊藤")
print(java)

#---------------------------------------------------------------------------

#資料構造の変更
menu = {"coffe", "milk", "juice"} # -> set {}
print(menu)
print(menu, type(menu))

menu = list(menu) # -> list []
print(menu, type(menu))

menu = tuple(menu) # -> tuple ()
print(menu, type(menu))

menu = set(menu) # -> set {}
print(menu,type(menu))

