#あなたの学校ではPythonコーディング大会を主催します。
#参加率を高めるためにコメントイベントを開催することにしました。
#コメント投稿者のうち抽選で1名はチキン、3名はコーヒークーポンをもらえます。
#抽選プログラムを作成しなさい。

#条件1：便宜上コメントは20名が作成し、IDは1～20と仮定
#条件2：コメント内容に関係なくランダムに抽選、ただし重複不可
#条件3：randomモジュールのshuffleとsampleを使用

#（出力例）
#-- 当選者発表 --
#チキン当選者 : 1
#コーヒー当選者 :
#-- おめでとうございます --

#（活用例）
#from random import *

#lst = [1,2,3,4,5]
#print(lst)
#shuffle(lst)
#print(lst)
#print(sample(lst, 1))

from random import *

users = list(range(1,21)) #条件1：便宜上コメントは20名が作成し、IDは1～20と仮定
print(users)

shuffle(users) #条件2：コメント内容に関係なくランダムに抽選
print(users) 

winners = sample(users,4)
print(winners) 
#条件2：コメント内容に関係なくランダムに抽選、ただし重複不可
#条件3：randomモジュールのshuffleとsampleを使用

chichen = winners[0]
coffee = winners[1:]

print("-- 当選者発表 --")
print("チキン当選者 : ",chichen)
print("コーヒー当選者 : ",coffee)
print("-- おめでとうございます --")





