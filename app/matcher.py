import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from app.model import encode

jobs = pd.read_csv("data/jobs.csv")
job_embeddings = np.load("embeddings/job_embeddings.npy")

def match(resume_text):
    resume_embedding = encode(resume_text)

    scores = cosine_similarity(
        [resume_embedding],
        job_embeddings
    )[0]

    jobs["score"] = scores
    return jobs.sort_values("score", ascending=False).head(5)
