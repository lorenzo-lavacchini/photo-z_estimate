import numpy as np
import pandas as pd

#Caricamento dei dataset
train_noCS = pd.read_csv("Data/train_noCS.csv")
test_noCS = pd.read_csv("Data/test_noCS.csv")

train_weakCS = pd.read_csv("Data/train_weakCS.csv")
test_weakCS = pd.read_csv("Data/test_weakCS.csv")

train_mildCS = pd.read_csv("Data/train_mildCS.csv")
test_mildCS = pd.read_csv("Data/test_mildCS.csv")

train_strongCS = pd.read_csv("Data/train_strongCS.csv")
test_strongCS = pd.read_csv("Data/test_strongCS.csv")

print(train_noCS)
print(test_noCS)

print(train_weakCS)
print(test_weakCS)

