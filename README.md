# Motif-based PageRank
### Introduction
This is the releasing code for our AAAI 2018 paper: "Ranking Users in Social Networks with Higher-Order Structures".

The following is an instruction to reproduce our experiments.

### Settings and Dependencies.
* CentOS release 6.9.
* Python 2.7.12.
* Numpy 1.11.0.
* Networkx 1.11.

### Datasets

We use three datasets for experiments. They are **DBLP, Epinion, Ciao**. The **DBLP** is provided by [Arminer](https://cn.aminer.org/billboard/citation) and we use the version V8, **Epinion, Ciao** are by provided by [Jiliang Tang](https://www.cse.msu.edu/~tangjili/trust.html). 
* DBLP:
  1. **author_name_id.txt** is the document which record the name of author and corresponding id which represent the node in the network.such as 'Jiawei Han;1' means the id for Jiawei Han is 1.
  2. **citation_network.txt** is the document which describe the relation network for all authors in forms of id. For example, '423;6151' means that the author with id of 423 cite the author with id of 6151.
  3. **h_index_all.txt** is the document which record the name of author and corresponding h-index. For example, 'Jiawei Han;151' means that the h-index of Jiawei Han is 151.
  4. **author_citation_domain.txt** records id, name and the number of citation for each author. For example, '1;Jiawei Han;2588' means that Jiawei Han has an id of 1 and has been cited by 2588 persons in DBLP network. 


* Epinions:
  1. **average_helpfulness_Epinion.txt** is the documents which record the average helpfulness of each person in this network. For example, '14192;4.095238' means that a person with id of 14192 own average helpfulness of 4.095238(the full score is 5).
  2. **trust_network_Epinion.txt** record the relation network for all persons in this network. For example, '9831;19832' means that person with id of 9831 think the evaluation of the person with id of 19832 is helpful.
  3. **average_indegree_Epinion.txt** recore the id and the indegree of this id in the network. For example, '16242;2024' means person with id of 16242 has degree of 2024.


* Ciao:
  1. **average_helpfulness_ciao.txt** is the documents which record the average helpfulness of each person in this network. For example, '12217;4.444444' means that a person with id of 12217 own average helpfulness of 4.444444(the full score is 5).
  2. **trust_network_Ciao.txt** record the relation network for all persons in this network. For example, '1;2' means that person with id of 1 think the evaluation of the person with id of 2 is helpful.
  3. **average_indegree_ciao.txt** recore the id and the indegree of this id in the network. For example, '256;95' means person with id of 256 has degree of 95.


### Motif-based PageRank

* DBLP:
  For example, we want to get the result where the motif we use is M7 and the $\alpha$ coefficient is 0.2, which is best in Top50

  1. we shall have the data which is **author_domain_id.txt, h_index_all.txt, itation_network.txt**

  2. modify the code of pagerank_motif_direct.py, in which there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

     ```python
     a, entry_unique = construct_motif('data/DBLP/citation_network.txt', 1, type, alpha)
     ```

     in this situation, we write **type = 'M7', alpha = 0.2**, and modify the output name in 

     ```python
     output = open(txt_name, 'w')
     ```

     The txt_name we need to specify, such as **'result_citation_M7_alpha0.2.txt'**

  3. we need to use the code of **experiment/DBLP/result_read.py** then  modify the row:

     ```
     f = open(txt_name) as f = open('result_citation_M7_alpha0.2.txt')
     ```

     and 

     ```
     output = open(txt_output_name, 'w')
     ```

     here txt_output_name is the final result. In txt_output_name, each row is author's id, name, pagerank_value. The name can also be **'result_citation_M7_alpha0.2.txt'** here.

* Epinions：
  For example, we want to get the result where the motif we use is M1 and the $\alpha$ coefficient is 0.4, which is best in Top50

  1. we shall have the data which is **average_helpfulness_Epinion.txt, trust_network_Epinion.txt**

  2. modify the code of pagerank_motif.py, there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

     ```python
     a, entry_unique = construct_motif('data/Epinions/trust_network_Epinion.txt', 1, type, alpha)
     ```

     in this situation, we write**type = 'M1', alpha = 0.4**, and modify the output name in 

     ```
     output = open(txt_name, 'w')
     ```

     The txt_name we need to specify, such as **'result_Epinions_M1_alpha0.4.txt'** In this result document, each row is person's id, pagerank_value.


* Ciao:
  For example, in order to get the result where the motif we use is M5 and the $\alpha$ coefficient is 0.08 which is best in Top50

  1. we shall have the data which is **average_helpfulness_ciao.txt, trust_network_ciao.txt**

  2. modify the code of pagerank_motif.py, there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

     ```python
     a, entry_unique = construct_motif('data/Ciao/trust_network_ciao.txt', 1, type, alpha)
     ```

     in this situation, we write **type = 'M5', alpha = 0.08**, and modify the output name in 

     ```python
     output = open(txt_name, 'w')
     ```

     The txt_name we need to specify, such as **'result_Ciao_M5_alpha0.08.txt'**In this result document, each row is person's id, pagerank_value.

### Evaluation

* DBLP
  once we get the result document from experiment, we can use the code of **ndcg_DBLP.py** in evaluate/DBLP file. 
  We need to modify the row: 

  ```
  txt_name = 'result_citation_M7_alpha0.2.txt'
  ```

  in order to get the result of M7 and $\alpha$ coefficient is 0.2. And **rank_value = 50** in order to get the ndcg value for TOP 50.

* Epinions
  once we get the result document from experiment, we can use the code of **ndcg_Epinions.py** in evaluate/Epinions file. 
  We need to modify the row:

  ```
  txt_name = 'result_Epinions_M1_alpha0.4.txt'
  ```

  in order to get the result of M1 and $\alpha$ coefficient is 0.4.

* Ciao
  once we get the result document from experiment, we can use the code of **ndcg_Ciao.py** in evaluate/Ciao file. 
  We need to modify the row:

  ```
  txt_name = 'result_Ciao_M5_alpha0.08.txt'
  ```

  in order to get the result of M5 and $\alpha$ coefficient is 0.08.

* rebuttal
  This is the extra experiment we did during review, the main idea is to indicate the significance of improvement between our motif-based method and two baseline wich is BPR and MPR. We select the 80% of nodes in the DBLP network using uniform distribution, and construct the subgraph. Then we run our experiments and evaluate to compute the ndcg value. Repeat this procedure for 30 times and the same is for the baseline such as BPR. So we can get the variable samples to compute the significance between them using t-test.

  1. motif_construct_direct_random.py : construct the subgraph and then compute the motif matrix.
  2. pagerank_motif_random.py: can compute the motif-pagerank result, if we want to compute the motif of 'M7' and $\alpha$ value of 0.2, then we can modify the row:

  ```python
  a, entry_unique = construct_motif('data/citation_network.txt', 1, 'M7', 0.2)
  ```

  this code will run the results for all 30 subgraphs. and if we want to compute the BPR:

  ```python
  a, entry_unique = construct_motif('data/citation_network.txt', 0, type, alpha_value)
  ```

  any type and alpha_value is ok.

  3. send the results to result_read_random.py and ndcg_DBLP_rebuttal.py, we can get the 30 ndcg value for each methods.
  4. using the above results and send it into t_test.py can get the final results which is the significance measurement.
### Baselines

DBLP:
1. IND：we need the data of author_citation_domain.txt in data/DBLP in which, each row is author's id, name and in-degree. And run the code of baseline/DBLP/ndcg_IND.py in which make sure that 

   ```
   txt_name = 'data/DBLP/author_citation_domain.txt'
   ```

2. BET: run the code in **baseline/DBLP/result_BET.py**, and send the result document into the evaluate code which is evaluate/DBLP/ndcg_DBLP.py.

3. CLO：run the code in **baseline/DBLP/result_CLO.py**, and send the result document into the evaluate code which is evaluate/DBLP/ndcg_DBLP.py.

4. BPR: like the procedure in experiment of DBLP, but we shall modify the code of experiment/DBLP/pagerank_motif_direct.py, in which there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

   ```
   a, entry_unique = construct_motif('data/citation_network.txt', 0, type, alpha)
   ```

   any type or alpha is ok. And get the result by **result_read.py** and **ndcg_DBLP.py** in turn.

5. WPR: like the procedure in experiment of DBLP, but we shall modify the code of **experiment/DBLP/pagerank_motif_direct.py**, in which there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

   ```
   a, entry_unique = construct_motif('data/citation_network.txt', 0, type, alpha)
   ```

   any type or alpha is ok. 
   and in the **experiment/DBLP/motif_construct_direct.py**, Comment the following row:

   ```
   adjacency_matrix.data = np.ones((1, lennn), dtype=np.float64)[0]
   ```

   And get the result by **result_read.py** and **ndcg_DBLP.py** in turn.

Epinions:
1. IND：we need the data of average_indegree_Epinion.txt in data/Epinions in which, each row is person's id, in-degree. And run the code of baseline/Epinions/ndcg_Epinion_IND.py in which make sure that **txt_name = 'data/Epinions/average_indegree_Epinion.txt'**

2. BET: run the code in **baseline/Epinions/result_Epinion_BET.py**, and send the result document into the evaluate code which is evaluate/Epinions/ndcg_Epinions.py.

3. CLO：run the code in **baseline/Epinions/result_Epinion_CLO.py**, and send the result document into the evaluate code which is evaluate/Epinions/ndcg_Epinions.py.

4. BPR: like the procedure in experiment of Epinions, but we shall modify the code of **experiment/Epinions/pagerank_motif.py**, in which there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

   ```
   a, entry_unique = construct_motif('data/Epinions/trust_network_Epinion.txt', 0, type, alpha)
   ```

   any type or alpha is ok. And get the result using **evaluate/Epinions/ndcg_Epinions.py** in turn.

5. WPR: like the procedure in experiment of Epinions, but we shall modify the code of **experiment/Epinions/pagerank_motif.py**, in which there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

   ```
   a, entry_unique = construct_motif('data/Epinions/trust_network_Epinion.txt', 0, type, alpha)
   ```

   any type or alpha is ok. 
   and in the **experiment/Epinions/motif_construct_direct.py**, Comment the following row:

   ```
   adjacency_matrix.data = np.ones((1, lennn), dtype=np.float64)[0]
   ```

   And get the result using **evaluate/Epinions/ndcg_Epinions.py** in turn.

Ciao:
1. IND：we need the data of average_indegree_ciao.txt in data/Ciao in which, each row is person's id, in-degree. And run the code of baseline/Ciao/ndcg_Ciao_IND.py in which make sure that 

   **txt_name = 'data/Ciao/average_indegree_ciao.txt'**

2. BET: run the code in **baseline/Ciao/result_Ciao_BET.py**, and send the result document into the evaluate code which is evaluate/Ciao/ndcg_Ciao.py.

3. CLO：run the code in **baseline/Ciao/result_Ciao_CLO.py**, and send the result document into the evaluate code which is evaluate/Ciao/ndcg_Ciao.py.

4. BPR: like the procedure in experiment of Ciao, but we shall modify the code of **experiment/Ciao/pagerank_motif.py**, in which there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

   ```
   a, entry_unique = construct_motif('data/Ciao/trust_network_ciao.txt', 0, type, alpha)
   ```

   any type or alpha is ok. And get the result using **evaluate/Ciao/ndcg_Ciao.py** in turn.

5. WPR: like the procedure in experiment of Ciao, but we shall modify the code of **experiment/Ciao/pagerank_motif.py**, in which there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

   ```
   a, entry_unique = construct_motif('data/Ciao/trust_network_ciao.txt', 0, type, alpha)
   ```

   any type or alpha is ok. 
   and in the **experiment/Ciao/motif_construct_direct.py**, Comment the following row:

   ```
   adjacency_matrix.data = np.ones((1, lennn), dtype=np.float64)[0]
   ```

   And get the result using **evaluate/Ciao/ndcg_Ciao.py** in turn.

   ​
