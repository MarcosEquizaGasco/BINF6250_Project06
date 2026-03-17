# Introduction
This project implements the Neighbor-Joining algorithm to construct a phylogenetic tree from a set of sequences. Pairwise sequence distances are first calculated using the Smith-Waterman local alignment algorithm. The Neighbor-Joining algorithm iteratively joins pairs of nodes, creates internal nodes and calculates branch lengths. The final tree is converted to Newick format and visualized.

# Pseudocode


```
1. Read input sequences from FASTA file.

2. Store sequences in a dictionary mapping the sequence ID to the sequence string

3. Compute a distance matrix:
        For each pair of sequences (i, j):
            Align the sequences using the Smith-Waterman alignment.
            Trace back the optimal alignment.
            Compute the normalized Hamming distance between the aligned sequences.
            Store the distance in a distance matrix

4. Initialize a tree structure with each sequence as a leaf node.

5. While n > 2:
        Compute a Q-matrix using the current distance matrix.
        identify the pair of nodes (i, j) with the minimum Q value.
        Calculate the branch lengths from i and j to a new internal node k (di and dj respectively).
        Add the internal node k to the tree and connect it to i and j with the branch lengths (di and dj).
        Create a new matrix of size n-1.
        Copy the distances between the remaining nodes into the new matrix.
        Calculate and save the distances between the new node k and the remaining nodes into the new matrix.
        Update the distance matrix.
        Update the list of node labels.
        Update n -> n -= 1.

6. Convert the final tree structure into a Newick string format.

7. Plot the phylogenetic tree from the Newick string.


```

# Successes

Our group worked collaboratively to understand the Neighbor Joining algorithm by researching the concept and discussing it via an example as a team. Through this approach, we were able to differentiate between neighbor joining and other additive tree reconstruction methods grounding our overall understanding of phylogenetic tree construction. We also reused our previous Smith-Waterman algorithm and adapted it so that it returned distance scores instead of similarity scores for our analysis. 

# Struggles
- Newick

  

# Personal Reflections
## Group Leader
Chantera: For this project, our group did not follow the approach discussed in class. Instead, we conducted additional research on the neighbor joining algorithm and developed our own implementation using the pseudocode provided in the notebook. This challenged me to think more critically about the algorithm rather than simply following the approach taught in class. I also enjoyed the opportunity to implement a class without a given framework skeleton as it gave me a chance to strengthen my object-oriented programming skills. Lastly, I learned so much from Marcos and Meghana. They were great teammates and their input deepened my understanding.

## Other member
Marcos:


Meghana: The concept for this project was a little difficult for me to understand initially, particularly how the internal nodes of the tree were created based on the calculated distances and branch lengths. Our group spent a lot of time discussing the algorithm and we spent a significant amount of time on the pseudocode, making sure each of us understood the process. Once I understood how it worked, the implementation was much simpler.

# Generative AI Appendix
As per the syllabus
