import numpy as np
import math
from scipy.stats import  ttest_ind


def read_top(txt_name, dict, dict2):
    f = open(txt_name)
    count = 0
    result_array = []
    while True:
        line = f.readline()
        if count >= 100:
            break
        if line:
            line = line.strip()
            line = line.split(';')
            name = line[1]
            h_index = dict2[name]
            print h_index
            if h_index < 30:
                h_index = 30
            if h_index > 30 and h_index < 60:
                h_index = 60
            if h_index > 60 and h_index < 100:
                h_index = 100
            result_array.append(h_index)
            count += 1
        else:
            break
    return result_array


def construct(txt_name):
    f = open(txt_name)
    user = {}
    count = 0
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            name = line[0]
            id = int(line[1])
            user[id] = name
            count += 1
        else:
            break
    return user


def construct2(txt_name):
    f = open(txt_name)
    user = {}
    count = 0
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            name = line[0]
            h_score = int(line[1])
            user[name] = h_score
            count += 1
        else:
            break
    return user


def read_ndcg(txt_name):
    f = open(txt_name)
    ndcg = []
    count = 0
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            ndcg_value = float(line)
            ndcg.append(ndcg_value)
            count += 1
        else:
            break
    return ndcg

if __name__ == "__main__":
    # txt_name3 = 'author_domain_id.txt'
    # dict = construct(txt_name3)
    # txt_name4 = 'h_index_all.txt'
    # dict2 = construct2(txt_name4)
    # txt_name = 'result_rank/alpha/M2/result_directM2_alpha1.0.txt'
    # txt_name2 = 'result_rank/alpha/M1/result_directM1_alpha0.2.txt'
    txt_name = 'random_set/M7_result.txt'
    txt_name2 = 'random_set/MPR_result.txt'
    # pagerank_array = read_top(txt_name, dict, dict2)
    # result_array = read_top(txt_name2, dict, dict2)
    result_array = read_ndcg(txt_name)
    pagerank_array = read_ndcg(txt_name2)
    print len(pagerank_array)
    print len(result_array)
    print ttest_ind(pagerank_array, result_array)
