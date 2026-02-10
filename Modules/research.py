import pandas as pd
import numpy as np

books = pd.read_csv('../Dataset/Books.csv', encoding='latin-1', low_memory=False)
print(books.head(5))