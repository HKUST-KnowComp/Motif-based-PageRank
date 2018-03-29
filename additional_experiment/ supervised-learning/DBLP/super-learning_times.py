# -*-coding: utf-8 -*-
from numpy import *
from motif_construct_direct import *
# from motif_construct_new import *
from scipy.sparse import diags
import networkx as nx
import pandas as pd
import time
import random
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
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


def construct(txt_name, name_to_id):
    # 构建name和H-index的dict
    f = open(txt_name)
    user = {}
    count = 0
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            name = line[0]
            id = name_to_id[name]
            score = int(line[1])
            user[id] = score
            # print name, score
            count += 1
        else:
            break
    return user


def compute_degree(a, maxnum):
    a = a.tocsr()
    print type(a)
    in_dict = {}
    out_dict = {}
    for number in range(maxnum):
        count_degree = 0
        for number_col in a.indices[a.indptr[number]:a.indptr[number + 1]]:
            if in_dict.get(number_col):
                in_dict[number_col] += 1
            else:
                in_dict[number_col] = 1
            count_degree += 1
        if not(in_dict.get(number)):
            in_dict[number] = 0
        out_dict[number] = count_degree
    return in_dict, out_dict


def compute(y_pre, y_test):
    df = pd.DataFrame({'A': y_pre, 'B': y_test})
    PLCC = df.corr()
    KROCC = df.corr('kendall')
    SROCC = df.corr('spearman')
    return PLCC['A']['B']


def read_name(txt_name):
    entry = []
    f = open(txt_name)
    while True:
        line = f.readline()
        if line:
            temp = []
            line = line.replace('\n', '')
            line = line.split(';')
            # print line
            for i in range(len(line)):
                temp.append(line[i])
            entry.append(temp)
        else:
            break
    dict_name = {}
    for number in range(len(entry)):
        dict_name[entry[number][0]] = int(entry[number][1])
    return dict_name


def get_ndcg(result1, result2):
    # 计算ndcg的值
    sum1 = 0
    sum2 = 0
    for i in range(len(result1)):
        sum1 += result1[i] * 1.0 / (np.log2(i+2))
        sum2 += result2[i] * 1.0 / (np.log2(i+2))
    return sum2 * 1.0 / sum1


def construct_close(txt_name):
    f = open(txt_name)
    close_dict = {}
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            id = int(line[0])
            score = float(line[1])
            close_dict[id] = score
        else:
            break
    return close_dict

if __name__ == "__main__":
    alpha = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    author_name_txt = 'author_domain_id.txt'
    name_to_id = read_name(author_name_txt)
    h_txt = 'h_index_all.txt'
    h_dict = construct(h_txt, name_to_id)
    output_txt = 'slearning/slearning_M7.txt'
    output = open(output_txt, 'w')
    for mmmm in range(10):
        for nn in range(len(alpha)):
            a, entry_unique = construct_motif_simple('data/citation_network.txt', 1, alpha[nn], 'M7')

            maxnum = len(entry_unique)
            entry_list = np.linspace(0, maxnum - 1, num=maxnum, dtype=np.int)
            # the new_netry_unique is the array which is picked randomly for training.
            new_entry_unique = random.sample(entry_list, 1500)
            
            test_array = np.load('test.npy')
            # the test_array is fixed for each motif type and dataset, we shall first store and then load it.
            # np.save('test.npy', test_array)

            in_dict, out_dict = compute_degree(a, len(entry_unique))
            G = nx.to_networkx_graph(a, create_using=nx.DiGraph())
            print("compute closeness")
            dict_t1 = nx.closeness_centrality(G)
            print("compute betweenness")
            dict_t2 = nx.betweenness_centrality(G)

            max_1 = np.max(in_dict.values())
            max_2 = np.max(out_dict.values())
            max_3 = np.max(dict_t1.values())
            max_4 = np.max(dict_t2.values())
            train_set_x = []
            train_set_y = []
            test_x = []
            test_y = []
            for mm in range(1500):
                # we use four features for each node we picked.
                num_element = new_entry_unique[mm]
                if not (in_dict.get(num_element)):
                    continue
                if not (out_dict.get(num_element)):
                    continue
                in_degree_num = in_dict[num_element] * 1.0 / max_1
                out_degree_num = out_dict[num_element] * 1.0 / max_2
                if out_degree_num == 0:
                    continue
                close = dict_t1[num_element] * 1.0 / max_3
                between = dict_t2[num_element] * 1.0 / max_4
                h_index = h_dict[entry_unique[num_element]]
                t_x = [in_degree_num, out_degree_num, close, between]
                train_set_x.append(t_x)
                train_set_y.append(h_index)

            for mm in range(len(test_array)):
                num_element = test_array[mm]
                if not (in_dict.get(num_element)):
                    continue
                if not (out_dict.get(num_element)):
                    continue
                in_degree_num = in_dict[num_element] * 1.0 / max_1
                out_degree_num = out_dict[num_element] * 1.0 / max_2
                close = dict_t1[num_element] * 1.0 / max_3
                between = dict_t2[num_element] * 1.0 / max_4
                h_index = h_dict[entry_unique[num_element]]
                t_x = [in_degree_num, out_degree_num, close, between]
                test_x.append(t_x)
                test_y.append(h_index)
            # print(test_x)
            svr = GridSearchCV(SVR(kernel='rbf'), cv=5,
                               param_grid={"C": np.logspace(-2, 2, 7), "gamma": np.logspace(-2, 2, 5)})
            svr.fit(train_set_x[:1500], train_set_y[:1500])
            y_predict = svr.predict(test_x)
            PLCC = compute(y_predict, test_y)
            y_predict = np.array(y_predict)
            test_y = np.array(test_y)
            RMSE = np.sqrt(np.mean((test_y - y_predict) ** 2))
            result = np.argsort(-y_predict)
            test_y = np.array(test_y)
            result2 = np.argsort(-test_y)
            result_array = []
            rank_array = []
            for iii in range(len(result)):
                result_array.append(test_y[result[iii]])
                rank_array.append(test_y[result2[iii]])
            ndcg = get_ndcg(rank_array, result_array)
            a = "%lf;%lf;%lf\n" % (PLCC, ndcg, RMSE)
            output.write(a)
    output.close()

