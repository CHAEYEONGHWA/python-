# 数値処理関数
print(abs(-5)) # 5
print(pow(4,2)) # 16
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 4
print(ceil(3.14)) # 4
print(sqrt(16)) # 4

# ランダム関数
from random import *
print(random()) # 0.0 < 1.0 ランダム数だす
print(random()*10) # 0.0 < 10.0 ランダム数だす
print(int(random()*10)) # 0 < 10 ランダム数だす
print:(int(random()*10)+1) # 1 ~ 10 ランダム数だす

print(int(random()*45)+1) # 1 ~ 45 ランダム数だす

print(randrange(1,45)) # 1 ~ 44 ランダム数だす
print(randrange(1,46)) # 1 ~ 45 ランダム数だす

print(randint(1,45)) # 1 ~ 45 ランダム数だす

#Quiz 
#あなたは最近にコーディング・スタディ会を新しく作りました。

#月4回スタディを実施するが、3回はオンライン、1回はオフラインとすることにしました。
#以下の条件に合ったオフライン会合日程を決定するプログラムを作成しなさい。

#条件1：ランダムで日付を選ばなければならない
#条件2：月ごとの日数は異なるため、最小日数の28日以内にすること
#条件3：毎月1～3日はスタディ準備のため除外

#(出力文例)
#オフラインスタディ会の日程は毎月x日と選定されました。

from random import *
date = randint(4, 28)
print("オフラインスタディ会の日程は毎月 " + str(date) + "日と選定されました。")
