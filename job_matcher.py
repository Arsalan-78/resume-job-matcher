import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_jobs_data(csv_path='jobs_dataset.csv'):
    return pd.read_csv(csv_path)

def match_jobs(resume_text, jobs_df, top_n=5):
    job_descriptions = jobs_df['description'].fillna('').tolist()
    titles = jobs_df['title'].fillna('Unknown').tolist()

    docs = [resume_text] + job_descriptions
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(docs)

    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    top_indices = cosine_sim.argsort()[-top_n:][::-1]

    return [(titles[i], cosine_sim[i]) for i in top_indices]