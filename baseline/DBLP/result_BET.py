import numpy as np
import networkx as nx

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


if __name__ == '__main__':
    txt_name_source = 'data/DBLP/citation_network.txt'
    G = construct_network(txt_name_source)
    dict_tt = nx.betweenness_centrality(G)
    txt_name2 = 'author_domain_id.txt'
    dict_name = name_dict(txt_name2)
    dict = sorted(dict_tt.items(), key=lambda item: item[1], reverse=True)
    output = open('baseline/betweenness_DBLP_rank.txt', 'w')
    for number in range(len(dict)):
        a = "%d;%s;%lf\n" % (int(dict[number][0]), dict_name[int(dict[number][0])], float(dict[number][1]))
        output.write(a)
    output.close()
