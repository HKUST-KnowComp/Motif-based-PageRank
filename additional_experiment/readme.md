There are some codes for additional experiments which are not concluded in the paper of AAAI.



#### Ensemble-method

* We do experiments to verify the ensemble methods for all the 3-node motifs. Here we average of all 7 3-node motif-based matrix and then utilize them for fusion.

  * DBLP

    For example, we want to get the result where the $\alpha$ coefficient is 0.2.

    We only need to modify the code in **pagerank_motif_direct.py** for one row:

    ```python
    a, entry_unique = construct_motif('data/DBLP/citation_network.txt', 1, 0.2)
    ```

    and modify the output name in 

    ```python
    output = open(txt_name, 'w')
    ```

    Then you can use the same method in **evaluation** to compute the NDCG value.

  * Epinions

    For example, we want to get the result where the $\alpha$ coefficient is 0.2.

    We only need to modify the code in **pagerank_motif.py** for one row:

    ```python
    a, entry_unique = construct_motif('data/Epinions/trust_network_Epinion.txt', 1, 0.2)
    ```

    and modify the output name in 

    ```python
    output = open(txt_name, 'w')
    ```

    Then you can use the same method in **evaluation** to compute the NDCG value.

  * ciao

    The situation is the same as **Epinions**.

    ​

#### non-linear-combination-method

* We do experiments to verify the methods for fusing the motif-based matrix with adj. matrix through nonlinear methods. For more details, please refer to the paper.

  * DBLP

    For example, we want to get the result where the motif we use is M7 and the $\alpha$ coefficient is 0.2.

    modify the code of **pagerank_motif_direct.py**, in which there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

    ```python
    a, entry_unique = construct_motif('data/DBLP/citation_network.txt', 1, 'M7', 0.2)
    ```

    And modify the output name in 

    ```python
    output = open(txt_name, 'w')
    ```

    The txt_name we need to specify, such as **'result_citation_M7_alpha0.2.txt'**. Then you can use the same method in **evaluation** to compute the NDCG value.

  * Epinions

    For example, we want to get the result where the motif we use is M1 and the $\alpha$ coefficient is 0.4。

    modify the code of **pagerank_motif.py**, there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

    ```python
    a, entry_unique = construct_motif('data/Epinions/trust_network_Epinion.txt', 1, 'M1', 0.4)
    ```

    And modify the output name in 

    ```python
    output = open(txt_name, 'w')
    ```

    The txt_name we need to specify, such as **'result_Epinions_M1_alpha0.4.txt'**. Then you can use the same method in **evaluation** to compute the NDCG value.

  * ciao

    The situation is the same as **Epinions**.

    ​

#### multiple-node-motifs

* These codes are utilized for constructing the 4-node-motif-based matrix and 5-node-motif-based matrix. They are all utilized for linear fusion like the situation of 3-node-motif.

  * 4-node-motif: These code are utilized to compute the situation with 4-node-motif-based matrix.

    **Note that we need first to get the member list of all subgraphs which is computed by mfinder1.21 here.** Here we use the sampling methods to obtain such list.

    * DBLP

      You must modify the code in **pagerank_motif_direct.py**, which is

      ```python
      a, entry_unique = construct_motif('data/DBLP/citation_network.txt', 1, '286', 0.4)
      ```

      where '286' is the id of one motif which is determined by mfinder software. You shall use the corresponding id in practical. 0.4 is the $\alpha$ value.

      In **node4-motif.py**, you can just add some motif whose id are not concluded in the function of **construct_four**.

      Once you obtain the results after run **pagerank_motif_direct.py**, you can use the same methods in **evaluation** to obtain the NDCG.

    * Epinions

      You must modify the code in **pagerank_motif.py**, which is

      ```python
      a, entry_unique = construct_motif('data/Epinions/trust_network_Epinion.txt', 1, '286', 0.08)
      ```

      where '286' is the id of one motif which is determined by mfinder software. You shall use the corresponding id in practical. 0.08 is the $\alpha$ value.

      In **node4-motif.py**, you can just add some motif whose id are not concluded in the function of **construct_four**.

      Once you obtain the results after run **pagerank_motif.py**, you can use the same methods in **evaluation** to obtain the NDCG.

    * ciao

      The situation is the same of **Epinions**.

      ​

  * 5-node-motif: These code are utilized to compute the situation with 5-node-motif-based matrix.

    **Note that we need first to get the member list of all subgraphs which is computed by mfinder1.21 here.** Here we use the sampling methods to obtain such list.

    * DBLP

      You must modify the code in **pagerank_motif_direct.py**, which is

      ```python
      a, entry_unique = construct_motif('data/DBLP/citation_network.txt', 1, '8734', 0.4)
      ```

      where '8734' is the id of one motif which is determined by mfinder software. You shall use the corresponding id in practical. 0.4 is the $\alpha$ value.

      In **node5-motif.py**, you can just add some motif whose id are not concluded in the function of **construct_five**.

      Once you obtain the results after run **pagerank_motif_direct.py**, you can use the same methods in **evaluation** to obtain the NDCG.

    * Epinions

      You must modify the code in **pagerank_motif.py**, which is

      ```python
      a, entry_unique = construct_motif('data/Epinions/trust_network_Epinion.txt', 1, '8734', 0.08)
      ```

      where '8734' is the id of one motif which is determined by mfinder software. You shall use the corresponding id in practical. 0.08 is the $\alpha$ value.

      In **node5-motif.py**, you can just add some motif whose id are not concluded in the function of **construct_five**.

      Once you obtain the results after run **pagerank_motif.py**, you can use the same methods in **evaluation** to obtain the NDCG.

    * ciao

      The situation is the same of **Epinions**.

    ​

 #### supervised-learning

* These codes are utilized to verify the effects of motifs through a supervised-learning problem.

  * DBLP

    You need to modify the **super-learning_times.py** which can compute the situation for all $\alpha$ value from 0~1 and repeat for ten times.

    ```python
    a, entry_unique = construct_motif_simple('data/DBLP/citation_network.txt', 1, alpha[nn], 'M7')
    ```

    You can re-write such code for the situation of 'M7' of 3-node-motif.

    please note that the training set is sampled randomly while the test set is fixed each time.

  * Epinions

    You need to modify the **super-learning_trust_times.py** which can compute the situation for all $\alpha$ value from 0~1 and repeat for ten times.

    ```python
    a, entry_unique = construct_motif_simple('data/Epinions/trust_network_Epinion.txt', 1, alpha[nn], 'M7')
    ```

    You can re-write such code for the situation of 'M7' of 3-node-motif.

  * ciao

    The situation is the same as **Epinions**.



#### sampling_method_testify

* These codes are utilized to prove that the motif-based matrix which is constructed by sampling methods are accurate enough.

  * 3-node-motif: We use the sampling methods to construct motif-based matrix and then linearly fuse them. We compare the results (the NDCG value) to ensure the results are close to the results which are computed by exact formula.

    * DBLP

      You must modify the code in **pagerank_motif_direct.py**, which is

      ```python
      a, entry_unique = construct_motif('data/DBLP/citation_network.txt', 1, '98', 0.4)
      ```

      where '98' is the id of one motif which is determined by mfinder software. You shall use the corresponding id in practical. 0.4 is the $\alpha$ value.

      In **node3-motif.py**, you can just add some motif whose id are not concluded in the function of **construct_three**.

      Once you obtain the results after run **pagerank_motif_direct.py**, you can use the same methods in **evaluation** to obtain the NDCG.

    * Epinions

      You must modify the code in **pagerank_motif.py**, which is

      ```python
      a, entry_unique = construct_motif('data/Epinions/trust_network_Epinion.txt', 1, '98', 0.08)
      ```

      where '98' is the id of one motif which is determined by mfinder software. You shall use the corresponding id in practical. 0.08 is the $\alpha$ value.

      In **node3-motif.py**, you can just add some motif whose id are not concluded in the function of **construct_three**.

      Once you obtain the results after run **pagerank_motif.py**, you can use the same methods in **evaluation** to obtain the NDCG.

    * ciao

      The situation is the same of **Epinions**.

  * RMSE: We use these codes to obtain the motif-based matrix computed by sampling and formula respectively. Then we compute the RMSE value of their element-wise difference.

    You can just run the code in each directory which will print the results.



#### anchor-motifs

* Add experiments with anchored motifs while we just use simple motifs in AAAI paper. The method to run code for each dataset is same with original experiments while we just modify the construction of motif-based function.

  * DBLP

    For example, we want to get the result where the motif we use is computed by $(U \cdot U^T) \odot B$ and the $\alpha$ coefficient is 0.2.

    1. we shall have the data which is **author_domain_id.txt, h_index_all.txt, citation_network.txt**

    2. modify the code of **pagerank_motif_direct.py**, in which there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

       ```python
       a, entry_unique = construct_motif('data/DBLP/citation_network.txt', 1, 0.2)
       ```

       Then we modify the function **motif_anchor**, which computes the motif-based matrix in **motif_construct_anchor.py**, according to the formula of $(U \cdot U^T) \odot B$. The situation for other anchor motif is similar. And modify the output name in 

       ```python
       output = open(txt_name, 'w')
       ```

       The txt_name we need to specify, such as **'result_citation_alpha0.2.txt'**. Then we can use the code in **evaluation** to compute the NDCG value.

  * ciao

    For example, in order to get the result where the motif we use is computed by $(U \cdot U^T) \odot B$ and the $\alpha$ coefficient is 0.08.

    1. we shall have the data which is **average_helpfulness_ciao.txt, trust_network_ciao.txt**

    2. modify the code of **pagerank_motif.py**, there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

       ```python
       a, entry_unique = construct_motif('data/Ciao/trust_network_ciao.txt', 1, 0.08)
       ```

       Then we modify the function **motif_anchor**, which computes the motif-based matrix in **motif_construct_anchor.py**, according to the formula of $(U \cdot U^T) \odot B$. The situation for other anchor motif is similar. And modify the output name in 

       ```python
       output = open(txt_name, 'w')
       ```

       The txt_name we need to specify, such as **'result_Ciao_alpha0.08.txt'**In this result document, each row is person's id, pagerank_value. Then we can use the code in **evaluation** to compute the NDCG value.

  * Epinions

    For example, we want to get the result where the motif we use is computed by $(U \cdot U^T) \odot B$ and the $\alpha$ coefficient is 0.4.

    1. we shall have the data which is **average_helpfulness_Epinion.txt, trust_network_Epinion.txt**

    2. modify the code of **pagerank_motif.py**, there is only one row we need to modify in order to compute results for different motif and $\alpha$ coefficients:

       ```python
       a, entry_unique = construct_motif('data/Epinions/trust_network_Epinion.txt', 1, 0.4)
       ```

       Then we modify the function **motif_anchor**, which computes the motif-based matrix in **motif_construct_anchor.py**, according to the formula of $(U \cdot U^T) \odot B$. The situation for other anchor motif is similar. And modify the output name in 

       ```python
       output = open(txt_name, 'w')
       ```

       The txt_name we need to specify, such as **'result_Epinions_alpha0.4.txt'** In this result document, each row is person's id, pagerank_value. Then we can use the code in **evaluation** to compute the NDCG value.