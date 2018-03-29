# -*-coding: utf-8 -*-
import numpy as np
from scipy.sparse import csr_matrix
import scipy.sparse
from scipy.sparse import diags


def normal_matrix(a):
    # 对于非对称的矩阵，我们的归一化的方式应该是按照行来进行归一化
    for number in range(0, np.size(a, 0)):
        if number % 10000 == 0:
            print "echo is %d" % number
        row_sum = a.getrow(number).sum()
        if row_sum == 0:
            continue
        else:
            for number_col in a.indices[a.indptr[number]:a.indptr[number+1]]:
                a[number, number_col] = a[number, number_col] / row_sum
    return a


def normal_matrix_new(a):
    # 对于对称的矩阵，我们可以使用矩阵相乘的方式来进行归一化，这样的话速度比较快。
    d = a.sum(0)
    d = np.array(d)
    d = d[0]
    dd = map(lambda x: 0 if x==0 else np.power(x, -0.5), d)
    D_matrix = diags(dd, 0)
    C = D_matrix.dot(a)
    C = C.dot(D_matrix)
    a = C
    return a

def row_read(txt_name, id):
    f = open(txt_name, 'r')
    result = []
    flag = False
    count = 0
    while True:
        line = f.readline()
        if line == ('subgraph id = %d\n' % int(id)):
            for i in range(4):
                line = f.readline()
            while True:
                line = f.readline()
                if line:
                    line = line.strip()
                    line = line.split('	')
                    if len(line) == 3:
                        result.append(line)
                        count += 1
                    else:
                        flag = True
                        break
        else:
            if flag == False:
                continue
            else:
                break
    print(len(result))
    return result


def construct_three(txt_name_out, entry_unique, type):
    motif_matrix = np.zeros((len(entry_unique), len(entry_unique)), dtype=np.float64)
    if type == '98':
        row_data = row_read(txt_name_out, 98)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_3][id_1] += 1
    if type == '102':
        row_data = row_read(txt_name_out, 102)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_3][id_1] += 1
    if type == '110':
        row_data = row_read(txt_name_out, 110)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_3][id_1] += 1
    if type == '238':
        row_data = row_read(txt_name_out, 238)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_3][id_1] += 1
            motif_matrix[id_3][id_2] += 1
    if type == '38':
        row_data = row_read(txt_name_out, 38)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_2][id_3] += 1
    if type == '108':
        row_data = row_read(txt_name_out, 108)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_3] += 1
            motif_matrix[id_3][id_1] += 1
    if type == '46':
        row_data = row_read(txt_name_out, 46)
        for number in range(len(row_data)):
            id_1 = np.where(entry_unique == int(row_data[number][0]))[0][0]
            id_2 = np.where(entry_unique == int(row_data[number][1]))[0][0]
            id_3 = np.where(entry_unique == int(row_data[number][2]))[0][0]
            motif_matrix[id_1][id_2] += 1
            motif_matrix[id_1][id_3] += 1
            motif_matrix[id_2][id_1] += 1
            motif_matrix[id_2][id_3] += 1
    return motif_matrix


def motif_times(adjacency_matrix, a, type):
    if type == 'M1':
        for i in range(a):
            print 'echo for motif is %d' % i
            adjacency_tran = np.transpose(adjacency_matrix)
            B_matrix_spare = adjacency_matrix.multiply(adjacency_tran)
            U_matrix = adjacency_matrix - B_matrix_spare
            U_matrix = np.abs(U_matrix)
            U_tran = np.transpose(U_matrix)
            result_1 = U_matrix.dot(U_matrix)
            result_1 = result_1.multiply(U_tran)
            adjacency_matrix = result_1
            adjacency_tran = np.transpose(adjacency_matrix)
            adjacency_matrix = adjacency_matrix + adjacency_tran
            adjacency_matrix = normal_matrix_new(adjacency_matrix)
            if len(adjacency_matrix.data) > 0:
                print np.max(adjacency_matrix.data), adjacency_matrix.nnz
    elif type == 'M2':
        for i in range(a):
            print 'echo for motif is %d' % i
            adjacency_tran = np.transpose(adjacency_matrix)
            B_matrix_spare = adjacency_matrix.multiply(adjacency_tran)
            U_matrix = adjacency_matrix - B_matrix_spare
            U_matrix = np.abs(U_matrix)
            U_tran = np.transpose(U_matrix)
            result_1 = B_matrix_spare.dot(U_matrix)
            result_1 = result_1.multiply(U_tran)
            result_2 = U_matrix.dot(B_matrix_spare)
            result_2 = result_2.multiply(U_tran)
            result_3 = U_matrix.dot(U_matrix)
            result_3 = result_3.multiply(B_matrix_spare)
            adjacency_matrix = result_1 + result_2
            adjacency_matrix = adjacency_matrix + result_3
            adjacency_tran = np.transpose(adjacency_matrix)
            adjacency_matrix = adjacency_matrix + adjacency_tran
            adjacency_matrix = normal_matrix_new(adjacency_matrix)
            if len(adjacency_matrix.data) > 0:
                print np.max(adjacency_matrix.data), adjacency_matrix.nnz
    elif type == 'M3':
        for i in range(a):
            print 'echo for motif is %d' % i
            adjacency_tran = np.transpose(adjacency_matrix)
            B_matrix_spare = adjacency_matrix.multiply(adjacency_tran)
            U_matrix = adjacency_matrix - B_matrix_spare
            U_matrix = np.abs(U_matrix)
            result_1 = B_matrix_spare.dot(B_matrix_spare)
            result_1 = result_1.multiply(U_matrix)
            result_2 = B_matrix_spare.dot(U_matrix)
            result_2 = result_2.multiply(B_matrix_spare)
            result_3 = U_matrix.dot(B_matrix_spare)
            result_3 = result_3.multiply(B_matrix_spare)
            adjacency_matrix = result_1 + result_2
            adjacency_matrix = adjacency_matrix + result_3
            adjacency_tran = np.transpose(adjacency_matrix)
            adjacency_matrix = adjacency_matrix + adjacency_tran
            adjacency_matrix = normal_matrix_new(adjacency_matrix)
            if len(adjacency_matrix.data) > 0:
                print np.max(adjacency_matrix.data), adjacency_matrix.nnz
    elif type == 'M4':
        for i in range(a):
            print 'echo for motif is %d' % i
            adjacency_tran = np.transpose(adjacency_matrix)
            B_matrix_spare = adjacency_matrix.multiply(adjacency_tran)
            result_1 = B_matrix_spare.dot(B_matrix_spare)
            result_1 = result_1.multiply(B_matrix_spare)
            adjacency_matrix = result_1
            adjacency_tran = np.transpose(adjacency_matrix)
            adjacency_matrix = adjacency_matrix + adjacency_tran
            adjacency_matrix = normal_matrix_new(adjacency_matrix)
            if len(adjacency_matrix.data) > 0:
                print np.max(adjacency_matrix.data), adjacency_matrix.nnz
    elif type == 'M5':
        for i in range(a):
            print 'echo for motif is %d' % i
            adjacency_tran = np.transpose(adjacency_matrix)
            B_matrix_spare = adjacency_matrix.multiply(adjacency_tran)
            U_matrix = adjacency_matrix - B_matrix_spare
            U_matrix = np.abs(U_matrix)
            U_tran = np.transpose(U_matrix)
            result_1 = U_matrix.dot(U_matrix)
            result_1 = result_1.multiply(U_matrix)
            result_2 = U_matrix.dot(U_tran)
            result_2 = result_2.multiply(U_matrix)
            result_3 = U_tran.dot(U_matrix)
            result_3 = result_3.multiply(U_matrix)
            adjacency_matrix = result_1 + result_2
            adjacency_matrix = adjacency_matrix + result_3
            adjacency_tran = np.transpose(adjacency_matrix)
            adjacency_matrix = adjacency_matrix + adjacency_tran
            adjacency_matrix = normal_matrix_new(adjacency_matrix)
            if len(adjacency_matrix.data) > 0:
                print np.max(adjacency_matrix.data), adjacency_matrix.nnz
    elif type == 'M6':
        for i in range(a):
            print 'echo for motif is %d' % i
            adjacency_tran = np.transpose(adjacency_matrix)
            B_matrix_spare = adjacency_matrix.multiply(adjacency_tran)
            U_matrix = adjacency_matrix - B_matrix_spare
            U_matrix = np.abs(U_matrix)
            U_tran = np.transpose(U_matrix)
            result_1 = U_matrix.dot(B_matrix_spare)
            result_1 = result_1.multiply(U_matrix)
            result_2 = B_matrix_spare.dot(U_tran)
            result_2 = result_2.multiply(U_tran)
            result_3 = U_tran.dot(U_matrix)
            result_3 = result_3.multiply(B_matrix_spare)
            adjacency_matrix = result_1 + result_2
            adjacency_matrix = adjacency_matrix + result_3
            adjacency_tran = np.transpose(adjacency_matrix)
            adjacency_matrix = adjacency_matrix + adjacency_tran
            adjacency_matrix = normal_matrix_new(adjacency_matrix)
            if len(adjacency_matrix.data) > 0:
                print np.max(adjacency_matrix.data), adjacency_matrix.nnz
    elif type == 'M7':
        for i in range(a):
            print 'echo for M7 motif is %d' % i
            adjacency_tran = np.transpose(adjacency_matrix)
            B_matrix_spare = adjacency_matrix.multiply(adjacency_tran)
            U_matrix = adjacency_matrix - B_matrix_spare
            U_matrix = np.abs(U_matrix)
            U_tran = np.transpose(U_matrix)
            result_1 = U_tran.dot(B_matrix_spare)
            result_1 = result_1.multiply(U_tran)
            result_2 = B_matrix_spare.dot(U_matrix)
            result_2 = result_2.multiply(U_matrix)
            result_3 = U_matrix.dot(U_tran)
            result_3 = result_3.multiply(B_matrix_spare)
            adjacency_matrix = result_1 + result_2
            adjacency_matrix = adjacency_matrix + result_3
            adjacency_tran = np.transpose(adjacency_matrix)
            adjacency_matrix = adjacency_matrix + adjacency_tran
            adjacency_matrix = normal_matrix_new(adjacency_matrix)
            if len(adjacency_matrix.data) > 0:
                print np.max(adjacency_matrix.data), adjacency_matrix.nnz
    return adjacency_matrix


def construct_motif(txt_name, type1, type2):
    # 先从txt中读取数据，txt中每一行的格式为a,b。表示的是a引用了b
    entry = []
    f = open(txt_name)
    while True:
        line = f.readline()
        if line:
            temp = []
            line = line.replace('\n', '')
            line = line.split(';')
            for i in range(len(line)):
                temp.append(int(line[i]))
            entry.append(temp)
        else:
            break
    spare_array_row = []
    spare_array_col = []
    spare_array_data = []
    entry_all = []
    for i in range(len(entry)):
        spare_array_row.append(entry[i][0])
        spare_array_col.append(entry[i][1])
        spare_array_data.append(1)
        entry_all.append(entry[i][0])
        entry_all.append(entry[i][1])
    entry_unique = np.unique(entry_all)
    # entry_unique中包含了所有的author的id
    newspare_array_row = []
    newspare_array_col = []
    counttt = 0
    # 为了要构建矩阵，需要将author的id进行连续性的编码
    for nnn in range(len(spare_array_row)):
        if counttt % 300000 == 0:
            print 'echo is %d' % counttt
        counttt += 1
        id1 = spare_array_row[nnn]
        id2 = spare_array_col[nnn]
        id1new = np.where(entry_unique == id1)[0][0]
        id2new = np.where(entry_unique == id2)[0][0]
        newspare_array_row.append(id1new)
        newspare_array_col.append(id2new)
    maxnum = len(entry_unique)
    adjacency_matrix = csr_matrix((spare_array_data, (newspare_array_row, newspare_array_col)), shape=(maxnum, maxnum), dtype = np.float64)
    data_array = adjacency_matrix.data
    lennn = data_array.shape[0]
    # 下面这一句adjacency_matrix.data主要是为了能够构建binary情况下的矩阵，如果需要weighted的矩阵，必须注释这句话
    adjacency_matrix.data = np.ones((1, lennn), dtype=np.float64)[0]
    txt_name_out = 'motif_detect/mfinder1.21/citation_fanmod3_MEMBERS.txt'
    result_D = construct_three(txt_name_out, entry_unique, type1)
    result_D = csr_matrix(result_D, dtype=np.float64)
    result_D_tran = np.transpose(result_D)
    result_D = result_D + result_D_tran
    # result_D is the motif-based-mat which is computed by sampling method.

    result_E = motif_times(adjacency_matrix, 1, type2)
    # result_E is the motif-based-mat which is computed by formula
    result_mm = result_D.tolil() - result_E.tolil()
    print(np.sqrt(np.mean(np.square(result_mm))))


if __name__ == '__main__':
    construct_motif('data/citation_network.txt','46', 'M7')
    # the first type is the motif id which is utilized by sampling method.
    # the second type is utilized for computing by formula.
