# 文字列
sentence = '私は大人です。'
print(sentence)
sentence2 = "pythonはかんたんです・"
print(sentence2)
sentence3= """
私は大人で、
pythonはかんたんです.
"""
print(sentence3)


jumin ="980918-1234567"

print("性別 : " + jumin[7])
print("年 : " + jumin[0:2]) # (0,1)
print("月 : " + jumin[2:4])
print("日 : " + jumin[4:6])
print("生年月日 : " + jumin[0:6])
print("生年月日 : " + jumin[:6])
print("生年月日 (逆に) : " + jumin[-7:])


python = "Python is Amazing."
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index +1)
print(index)

print(python.find("n"))
print(python.find("Java")) # 含まれてない単語はー1が出る
#print(python.index("Java"))# 含まれてない単語はエラーが出る
print("hi")

print(python.count("n"))

#-------------------------------------------------------------------------------------------

#方法1
print("私は%d歳です" % 20)
print("私は%sが好きです" % "python")
print("Appleは%cで始まります" % "A")
# %s 
print("私は%s歳です" % 20)
print("わたしは%s色と%s色が好きです" % ("blue", "red"))

#方法2
print("私は{}歳です" .format(20))
print("わたしは{}色と{}色が好きです" . format("blue", "red"))
print("わたしは{0}色と{1}色が好きです" . format("blue", "red"))
print("わたしは{1}色と{0}色が好きです" . format("blue", "red"))

#方法3
print("私は{age}歳で、{color}色が好きです" . format(age = 20, color = "red"))
print("私は{age}歳で、{color}色が好きです" . format(color = "red", age = 20, ))

#方法4 (v3.6~)
age = 20
color = "red"
print(f"私は{age}歳で、{color}色が好きです")

#------------------------------------------------------------------------------------------
# \n
print("A is apple \nB is bag")  
# \"\"  or  \'\'
print("A is\"apple\"") 
# \\ -> \
print("C:\\Users\\User>")
# \r 
print("Red Apple\rPine") # PineApple
# \b (一文字削除)
print("Redd\bApple") # RedApple
# \t
print("Red\tApple") # Red     Apple

#------------------------------------------------------------------------------------------
#Quiz）サイトごとにパスワードを作成するプログラムを作成しなさい。

#例）http://google.com

#ルール1：http:// の部分は除外する。
#ルール2：最初に現れるドット（.）以降の部分は除外する。
#ルール3：残った文字列について、先頭から3文字, 文字列の長さ, 文字列の中に含まれる e の個数, 最後に ! をつなげてパスワードを作成する。

#例）生成されるパスワード：nav51!


url = "http://google.com"
a_url = url.replace("http://", "") #ルール1
print(a_url)
a_url = a_url[:a_url.index(".")] #ルール2
print(a_url)
password = a_url[:3] + str(len(a_url)) + str(a_url.count("e")) + "!" #ルール3
print("生成されるパスワード：" + password)
