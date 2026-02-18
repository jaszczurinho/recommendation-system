import pandas as pd
import re
from sentence_transformers import SentenceTransformer

data = pd.read_excel('../output/summrized_preprocessed_descriptions_V1.xlsx', index_col=0)

def clean_text(input_text):   
    clean_text = re.sub('<[^<]+?>', '', input_text) 
    clean_text = re.sub('\s+', ' ', clean_text)
    
    return clean_text


data["preprocessed_summaries"] = data["summaries"].apply(clean_text)

embedding_model = "msmarco-distilbert-cos-v5"
embedder = SentenceTransformer(embedding_model)

embeddings = embedder.encode_document(data["summaries"].to_list(),
                            show_progress_bar=True)

data["embeddings"] = embeddings.tolist()

data.to_parquet('../output/data_with_embeddings.parquet', engine = 'pyarrow')