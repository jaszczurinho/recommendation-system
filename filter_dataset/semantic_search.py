import torch
from sentence_transformers import SentenceTransformer
import pandas as pd
from typing import List

def semantic_mapping(user_values: List[str], corpus: List[str], embedder: SentenceTransformer, top_k: int = 2):
    if not user_values or not corpus:
        return []
    
    corpus_emb = embedder.encode(corpus, convert_to_tensor=True)
    queries_emb = embedder.encode(user_values, convert_to_tensor=True)
    similarity_scores = embedder.similarity(queries_emb, corpus_emb)
    
    mapped_words = []
    
    for i in range(len(user_values)):
        scores, indices = torch.topk(similarity_scores[i], k=top_k)
        matches_for_word = [corpus[idx.item()] for idx in indices]
        mapped_words.append(matches_for_word)

    return mapped_words
