# -*-coding: utf-8 -*-
import numpy as np
import math


def read_top(txt_name, dict, K):
    # 从指定的result文件中读取前K个，也就是TOP K
    f = open(txt_name)
    count = 0
    result_array = []
    name_array = []
    while True:
        line = f.readline()
        if count >= K:
            break
        if line:
            line = line.strip()
            line = line.split(';')
            name = line[1]
            score = dict[name]
            # print name, score
            if score < 30:
                continue
            result_array.append(score)
            name_array.append(name)
            count += 1
        else:
            break
    return result_array, name_array


def construct(txt_name):
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
            score = int(line[1])
            user[name] = score
            # print name, score
            count += 1
        else:
            break
    return user


def get_ndcg(result1, result2):
    # 计算ndcg的值
    sum1 = 0
    sum2 = 0
    for i in range(len(result1)):
        sum1 += result1[i] * 1.0 / (np.log2(i+2))
        sum2 += result2[i] * 1.0 / (np.log2(i+2))
    return sum2 * 1.0 / sum1


if __name__ == '__main__':
    txt_name3 = 'h_index_all.txt'
    # 是有author的H-index的文件
    dict_author = construct(txt_name3)
    txt_name = 'data/DBLP/author_citation_domain.txt'
    # 在这里改变结果文件就可以获得不同的motif结果的下的ndcg
    rank_value = 50
    rank_array, name_array = read_top(txt_name, dict_author, rank_value)
    # 下面构建的是理想情况下的排名（按照H-index）
    result = {}
    for i in range(len(rank_array)):
        score = dict_author[name_array[i]]
        result[name_array[i]] = score
    result_array = []
    dict = sorted(result.items(), key=lambda item: item[1], reverse=True)
    for i in range(len(dict)):
        result_array.append(dict[i][1])

    # 得到了rank的排列以及理想的排列之后，可以用我们的ndcg计算的函数进行计算
    print len(result_array)
    print len(rank_array)
    score = get_ndcg(result_array, rank_array)
    print score
