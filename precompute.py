import pandas as pd
import numpy as np
from app.model import encode

jobs = pd.read_csv("data/jobs.csv")

embeddings = [encode(j) for j in jobs["description"]]

np.save("embeddings/job_embeddings.npy", embeddings)
