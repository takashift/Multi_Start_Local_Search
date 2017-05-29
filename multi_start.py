import sys
import numpy as np
#import random

# 初期解(引数)
P = int(sys.argv[1])
# 順列の数
N = 24

list = range(N)

num = np.arange(4)
index = np.zeros(4, dtype = np.int_)
ans = np.zeros((10, 4, 4), dtype = np.int_)

# 重複無しでリストから値を取得
n = np.random.choice(list, P, replace = False)

# print(i)

# 数字から順列をつくるアルゴリズム
# http://itakanaya9.hatenablog.com/entry/2014/02/17/121428
for i in range(P):
    # n = random.randint(0, N)
    b = n[i] / 2
    index[2] = n[i] % 2
    c = b / 3
    index[1] = b % 3
    index[0] = c % 4
    num_tmp = num
    # print("index", index)
    # print("num", num_tmp)

    for j in range(4):
        ans[i,0,j] = num_tmp[index[j]]
        if j < 4:
            # print(index[j])
            num_tmp = np.delete(num_tmp, index[j])
        # print(j, num_tmp)

    print("P", i,  "=", '(', ans[i,0,0],ans[i,0,1],ans[i,0,2],ans[i,0,3], ')')
    # if ans[0] == 1:

    for k in range(3):
        ans[i,k+1] = ans[i,0]
        tmp = ans[i,k+1,0+k]
        ans[i,k+1,0+k] = ans[i,k+1,1+k]
        ans[i,k+1,1+k] = tmp
        print("P", i, k+1, "=", '(', ans[i,k+1,0],ans[i,k+1,1],ans[i,k+1,2],ans[i,k+1,3], ')')

    print()

    
