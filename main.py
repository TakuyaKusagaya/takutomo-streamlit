import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

#タイトルを書く
st.title('Streamlit超入門')

#普通の文字を書く
st.write('プログレスバーの表示')

#プログレスバーを作る
'Start!!'

latest_iteration = st.empty()#空の箱を作る
bar = st.progress(0)

for i in range(100):# iを0から99まで順に繰り返す
    latest_iteration.text(f'Iteration {i+1}')#数字を順番に表示
    bar.progress(i + 1)# プログレスバーを順次延ばす(増やす)
    time.sleep(0.1)# 1 -> 2 の間に0.1秒休止、大きい数字でカウンターが遅くなる

'Done!!!!!'



#2カラムレイアウト
left_column, right_column = st.beta_columns(2)#今後 st.columns() になる
buttom = left_column.button('押すと右カラムに文字を表示')
if buttom:
    right_column.write('ここが右カラムです。')
    
#エキスパンダー
expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander1 = st.beta_expander('問い合わせ2')
expander1.write('問い合わせ2の回答')
expander1 = st.expander('問い合わせ3')# st.expander で書式が使える
expander1.write('問い合わせ3の回答')