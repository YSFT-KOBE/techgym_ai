#AI-TECHGYM-N-5

import pandas as pd

#indexとcolumnsの指定
feature1 =['gender','age','win','lose','draw']
feature2 =['性別','年齢','勝ち','負け','あいこ']
id = ['100','101','102','103','104','105','106','107','108','109']
num = ['0','1','2','3','4','5','6','7','8','9']

hand = {'性別'  :['男性','男性','女性','男性','女性','男性','女性','女性','男性','男性'],
    '年齢'  :['30代','20代','10代','10代','40代','50代','40代','10代','20代','10代'],
    '勝ち'  :[20,21, 4,60,14,10,12,19,12,14],
    '負け'  :[24,15,35, 3,35,29, 2,12,11,43],
    'あいこ':[15,40,34,29,14, 4,22,17,12,10]}
hand_df1 = pd.DataFrame(hand)

#必要があれば表示
#display(hand_df1)

#データフレームのコピー
hand_df2 = 

#index,columnsを複数つけ、さらに名前を指定する




#表示
display(hand_df2)

#index columnsのレベル1を削除する
hand_df2.columns = 
hand_df2.index = 

#Columnがgenderのデータのみ表示


#Indexが106のところを削除,行方向に合計する場合は、axisパラメータを0に設定


#Columnがgenderのところを削除,列方向に合計する場合は、axisパラメータを1に設定
