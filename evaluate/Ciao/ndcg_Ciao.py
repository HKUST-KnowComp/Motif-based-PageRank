# -*-coding: utf-8 -*-
import numpy as np
import math


def read_top(txt_name, dict, limit):
    # 从指定的result文件中读取前K个，也就是TOP K
    f = open(txt_name)
    count = 0
    result_array = []
    id_array = []
    while True:
        line = f.readline()
        if count >= limit:
            break
        if line:
            line = line.strip()
            line = line.split(';')
            id = int(line[0])
            if dict.get(id):
                score = dict[id]
            else:
                continue
            result_array.append(score)
            id_array.append(id)
            count += 1
        else:
            break
    return result_array, id_array


def construct(txt_name):
    # 构建id和平均的helpfulness的dict
    f = open(txt_name)
    user = {}
    count = 0
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            id = int(line[0])
            score = float(line[1])
            user[id] = score
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
    txt_name3 = 'data/Ciao/average_helpfulness_ciao.txt'
    # 是有id以及其平均的helpfulness的文件
    dict = construct(txt_name3)
    txt_name = 'result_Ciao_M5_alpha0.08.txt'
    # 在这里改变结果文件就可以获得不同的motif结果的下的ndcg
    a = [100, 500, 50, 10]
    for nn in range(len(a)):
        rank_array, id_array = read_top(txt_name, dict, a[nn])
        # 下面构建的是理想情况下的排名（按照平均的helpfulness）
        result = {}
        for i in range(len(rank_array)):
            score = dict[id_array[i]]
            result[id_array[i]] = score
        result_array = []
        dict_temp = sorted(result.items(), key=lambda item: item[1], reverse=True)
        for i in range(len(dict_temp)):
            result_array.append(dict_temp[i][1])
        # 得到了rank的排列以及理想的排列之后，可以用我们的ndcg计算的函数进行计算
        print len(result_array), len(rank_array)
        score = get_ndcg(result_array, rank_array)
        print score

