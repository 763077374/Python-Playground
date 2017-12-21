#coding:utf-8
#author:zhanghua
#python学习
def miniEditDistance(s1,s2):
    '''计算将s1转换到s2的最小编辑距离'''
    len1 = len(s1)
    len2 = len(s2)

    #创建一个二维数组
    #满足m[i][j] =0,0<=i<=len1,0<=j<=len2
    m = [None]*(len1+1)

    for i in range(len1+1):
        m[i] =[0]*(len2+1)


    #横向、纵向设置初始化操作次数
    for i in range(1,len1+1):
        m[i][0] =i
    for j in range(1,len2+1):
        m[0][j] = j


    #计算最优解
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            coust =1
            if s1[i-1] ==s2[j-1]:coust =0
            replaceCost = m[i-1][j-1] +coust
            removeCost = m[i-1][j]+1
            insertCost = m[i][j-1]+1
            m[i][j] = min(replaceCost,removeCost,insertCost)
    print(m)
    return m[len1][len2]

if __name__ == '__main__':
    print(miniEditDistance('GCTAC','CTCA'))