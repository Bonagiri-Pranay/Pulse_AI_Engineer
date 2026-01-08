from src.utils.embedding_utils import get_embeddings
from src.utils.clustering_utils import cluster_embeddings
from src.utils.gemini_client import call_llm

def merge_topics_agent(topics):
    embs = get_embeddings(topics)
    labels = cluster_embeddings(embs)

    topic_groups = {}
    for t, label in zip(topics, labels):
        topic_groups.setdefault(label, []).append(t)

    final_topics = {}
    for label, items in topic_groups.items():
        merged = call_llm(
            "You merge similar phrases into one canonical topic.",
            f"Merge these phrases: {items}"
        )
        final_topics[label] = merged

    return final_topics
