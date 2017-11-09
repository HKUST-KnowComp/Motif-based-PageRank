import numpy as np
import networkx as nx


def construct_network(txt_name):
    f = open(txt_name)
    G = nx.DiGraph()
    count = 0
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            node1 = int(line[0])
            node2 = int(line[1])
            count += 1
            G.add_node(node1)
            G.add_node(node2)
            G.add_edge(node1, node2)
        else:
            break
    return G

def name_dict(txt_name):
    f = open(txt_name)
    count = 0
    dict_name = {}
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            name = line[0]
            id = int(line[1])
            dict_name[id] = name
            count += 1
        else:
            break
    return dict_name


if __name__ == '__main__':
    txt_name = 'data/Epinions/trust_network_Epinion.txt'
    G = construct_network(txt_name)
    dict_result = nx.betweenness_centrality(G)
    txt_name_result = 'betweenness_Epinion.txt'
    output = open(txt_name_result, 'w')
    dict_tt = sorted(dict_result.items(), key=lambda item: item[1], reverse=True)
    for number in range(len(dict_tt)):
        a = "%d;%lf\n" % (dict_tt[number][0], float(dict_tt[number][1]))
        output.write(a)
    output.close()
    




