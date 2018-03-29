# -*-coding: utf-8 -*-
from numpy import *
from motif_construct_anchor import *
from scipy.sparse import diags
MAX_TIME = 30000

# 按照我们需要做的矩阵的要求，如果是direct，则从motif_construct_direct中import


def graphMove_new(a):
    # 这个函数是将我们得到的矩阵进行归一化的处理，用的方法是按照行进行
    for number in range(0, np.size(a, 0)):
        if number % 10000 == 0:
            print "echo is %d" % number
        row_sum = a.getrow(number).sum()
        if row_sum == 0:
            continue
        else:
            for number_col in a.indices[a.indptr[number]:a.indptr[number+1]]:
                a[number, number_col] = a[number, number_col] / row_sum
    a = transpose(a)
    return a


def graphMove_newest(a):
    # 这个函数是将我们得到的矩阵进行归一化的处理的另一种方式，只能对于对称的矩阵
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
        if count % 10000 == 0:
            print "echo is %d" % count
        v = p * m.dot(v) + ((1 - p) / n) * e
        count = count + 1
    return v


if __name__ == "__main__":
    # 如果从direct的网络中进行，则应该使用如下的语句获得矩阵，a在这里1表示的是motif的阶数，
    # 阶数为0即可得到pagerank在citation网络上的结果，'M6'表示我们做的是哪一种motif,alpha为融合参数

    a, entry_unique = construct_motif('data/citation_network.txt', 1, 0.4)

    # M = graphMove_newest(a)
    M = graphMove_new(a)
    pr = firstPr(M)
    p = 0.8  # 引入浏览当前网页的概率为p,假设p=0.8
    v = pageRank(p, M, pr)  # 计算pr值
    # 将我们的结果写入
    output = open('result_citation_M6_alpha0.4.txt', 'w')
    for i in range(len(v)):
        a = "%lf %d\n" % (v[i], entry_unique[i])
        output.write(a)
    output.close()
