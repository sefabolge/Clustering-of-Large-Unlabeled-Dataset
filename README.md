# Clustering-of-Large-Unlabeled-Dataset
LARGE-SCALE CLUSTERING
CLUSTERING OF LARGE UNLABELED DATASETS

----OVERVIEW ----

Real world data is frequently unlabeled and can seem completely random. In these sort of situations, unsupervised learning techniques are a great way to find underlying patterns. This project looks at one such algorithm, KMeans clustering, which searches for boundaries separating groups of points based on their differences in some features.

The goal of the project is to implement an unsupervised clustering algorithm using a distributed computing platform. You will implement this algorithm on the stack overflow user base to find different ways the community can be divided, and investigate what causes these groupings.

The clustering algorithm must be designed in a way that is appropriate for data intensive parallel computing frameworks. Spark would be the primary choice for this project, but it could also be implemented in Hadoop MapReduce. Algorithm implementations from external libraries such as Spark MLib may not be utilised; the code must be original from the students. However, once the algorithm is completed, a comparison between your own results and that generated by MLlib could be interesting and aid your investigation.

Stack Overflow is the main dataset for this project, but alternative datasets can be adopted after consultation with the module organiser. Additionally, different clustering algorithms may be utilised, but this must be discussed and approved y the module organiser. 


---Read ME----

./K-means: presents the implementation of the K-Means clustering algorithm. Inside this folder, we have kmeans_language.py, created for the language analysis and kmeans.py, created for the other analysis performed.

./FeatureExtraction_MLlib : presents the methods and codes to extract the information from the database and how to use MLlib to perform K-means. The codes in this folder were used not only to produce the comparison but also to produce a Kmeans vector file, to be used with our implementation of the algorithm.

./Plotting: Here we have the plot codes together with the raw data to be plot 
