'''
摂動によって得られた近傍解で暫定解（初期解）を一回だけ更新する
'''

import sys
import numpy as np

# 初期解の数(引数)
P = int(sys.argv[1])
# 順列の数
N = 24

# 割当て問題(横方向に各A,B,C,Dそれぞれの能力、縦方向は処理する問題に対応)
A = [6, 1, 9, 3]
B = [2, 5, 7, 8]
C = [6, 3, 5, 4]
D = [3, 5, 2, 1]

# 組み込み関数で重複無しの乱数値を得るには事前に数列のリストを作成する必要がある
list = range(N)

num = np.arange(4)
index = np.zeros(4, dtype = np.int_)
ans = np.zeros((P, 4, 4), dtype = np.int_)
ans_old = np.zeros((N, 4, 4), dtype = np.int_)
sum = np.zeros(P*4, dtype = np.int_)
l = 0
h = 0
same = False

# 重複無しでリストからランダムに値を取得
n = np.random.choice(list, P, replace = False)

# 数字から順列をつくるアルゴリズム
# http://itakanaya9.hatenablog.com/entry/2014/02/17/121428
for i in range(P):
    b = n[i] / 2
    index[2] = n[i] % 2
    c = b / 3
    index[1] = b % 3
    index[0] = c % 4
    num_tmp = num

    for j in range(4):
        ans[i,0,j] = num_tmp[index[j]]
        if j < 4:
            num_tmp = np.delete(num_tmp, index[j])

    # 目的関数の計算
    sum[l] = A[ans[i,0,0]] + B[ans[i,0,1]] + C[ans[i,0,2]] + D[ans[i,0,3]]
    print("P", i, "=", '(', ans[i,0,0],ans[i,0,1],ans[i,0,2],ans[i,0,3], ') Ans =', sum[l])
    l += 1

    # 隣同士を先頭から順番に入れ替える摂動
    for k in range(3):
        ans[i,k+1] = ans[i,0]
        tmp = ans[i,k+1,0+k]
        ans[i,k+1,0+k] = ans[i,k+1,1+k]
        ans[i,k+1,1+k] = tmp

        # 目的関数の計算
        sum[l] = A[ans[i,k+1,0]] + B[ans[i,k+1,1]] + C[ans[i,k+1,2]] + D[ans[i,k+1,3]]
        print("P", i, k+1, "=", '(', ans[i,k+1,0],ans[i,k+1,1],ans[i,k+1,2],ans[i,k+1,3], ') Ans =', sum[l])
        l += 1

    print()

# 最小の値の取得
min = np.min(sum)
print("min =", min)

# 最小の値のインデックスを取得
# ！np.where の出力は2次元配列なので注意！ min[0]を使う！
min = np.where(sum == min)

for m in min[0]:
    # 割り算の結果が int じゃないので変換する
    trns = int(m/4)
    # 一致しているものがあればパス
    for old in ans_old:
        if (ans[trns, m%4] == old).all():
            same = True
    if same == True:
        same = False
        continue

    print("(", ans[trns, m%4, 0], ans[trns, m%4, 1], ans[trns, m%4, 2], ans[trns, m%4, 3], ")")
    ans_old[h] = ans[trns, m%4]
    h += 1
