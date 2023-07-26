import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('Case Study - Transaction.csv', sep=';')

df = df.groupby('CustomerID').agg({'TransactionID': 'count',
                                   'Qty': 'sum',
                                   'TotalAmount': 'sum'
                                   }).reset_index()
df.columns = ['CustomerID', 'TransactionCount', 'TotalQty', 'TotalAmount']
df.set_index('CustomerID', inplace=True)

model = KMeans(n_clusters=3)
model.fit(df)
label = model.labels_
centroid = model.cluster_centers_

plt.figure(figsize=(9, 5))
plt.scatter(x=df["TransactionCount"], y=df["TotalQty"], c=label)
plt.scatter(x=centroid[:,0], y=centroid[:,1], s=100, c="red")
plt.title("Segmentasi Customer Berdasarkan Total Quantity dan Transaction Count")
plt.xlabel("Transaction Count")
plt.ylabel("Total Qty")
plt.show()

plt.figure(figsize=(9, 5))
plt.scatter(x=df["TransactionCount"], y=df["TotalAmount"], c=label)
plt.scatter(x=centroid[:,0], y=centroid[:,2], s=100, c="red")
plt.title("Segmentasi Customer Berdasarkan Total Amount dan Transaction Count")
plt.xlabel("Transaction Count")
plt.ylabel("Total Amount")
plt.show()

plt.figure(figsize=(9, 5))
plt.scatter(x=df["TotalQty"], y=df["TotalAmount"], c=label)
plt.scatter(x=centroid[:,1], y=centroid[:,2], s=100, c="red")
plt.title("Segmentasi Customer Berdasarkan Total Amount dan Total Quantity")
plt.xlabel("Transaction Count")
plt.ylabel("Total Qty")
plt.show()

