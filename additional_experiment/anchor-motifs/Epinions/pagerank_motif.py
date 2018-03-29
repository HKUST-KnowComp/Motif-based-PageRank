# -*-coding: utf-8 -*-
from numpy import *
# from motif_construct_direct import *
from motif_construct_anchor import *
from scipy.sparse import diags
MAX_TIME = 30000


def graphMove(a):
    # 构造转移矩阵, we will construct the transfer matrix
    b = transpose(a)
    # b为a的转置矩阵
    c = zeros((a.shape), dtype=float)
    for j in range(a.shape[1]):
        if j % 1000 == 0:
            print "echo is %d" % j
        if b[j].sum() == 0:
            continue
        else:
            c[j] = b[j] / (b[j].sum())
    c = transpose(c)
    return c


def graphMove_new(a):
    for number in range(0, np.size(a, 0)):
        if number % 10000 == 0:
            print "echo is %d" % number
        # row_sum = np.sum(a[number, :].toarray())
        row_sum = a.getrow(number).sum()
        if row_sum == 0:
            continue
        else:
            for number_col in a.indices[a.indptr[number]:a.indptr[number+1]]:
                a[number, number_col] = a[number, number_col] / row_sum
    a = transpose(a)
    return a


def graphMove_newest(a):
    d = a.sum(0)
    d = np.array(d)
    d = d[0]
    dd = map(lambda x: 0 if x==0 else np.power(x, -0.5), d)
    D_matrix =diags(dd, 0)
    C = D_matrix.dot(a)
    C = C.dot(D_matrix)
    a = C
    a = transpose(a)
    return a


def firstPr(c):
    # pr值得初始化
    pr = zeros((c.shape[0], 1), dtype=float)
    # 构造一个存放pr值得矩阵
    for i in range(c.shape[0]):
        pr[i] = float(1) / c.shape[0]
    return pr


def pageRank(p, m, v):
    e = np.ones((m.shape[0], 1))
    n = m.shape[0]
    count = 0
    print m.shape
    print v.shape
    # m_spare = csr_matrix(m)
    # we will use the equation to compute the value of pagerank 计算pageRank值
    while count <= MAX_TIME:
        # 判断pr矩阵是否收敛,(v == p*dot(m,v) + (1-p)*v).all()判断前后的pr矩阵是否相等，若相等则停止循环
        if count % 10000 == 0:
            print "echo is %d" % count
        v = p * m.dot(v) + ((1 - p) / n) * e
        count = count + 1
    return v


if __name__ == "__main__":
    a, entry_unique = construct_motif('data/Epinions/trust_network_Epinion.txt', 1, 0.4)
    M = graphMove_new(a)
    pr = firstPr(M)
    p = 0.8  # 引入浏览当前网页的概率为p,假设p=0.8
    v = pageRank(p, M, pr)  # 计算pr值
    result_temp = {}
    for number in range(len(v)):
        result_temp[entry_unique[number]] = v[number]
    dict = sorted(result_temp.items(), key=lambda item: item[1], reverse=True)
    output = open('result_Epinions_M1_alpha0.4.txt', 'w')
    for i in range(len(dict)):
        a = "%d;%lf\n" % (dict[i][0], dict[i][1])
        output.write(a)
    output.close()
