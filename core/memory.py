import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection("stilgar_memory")

embeddingsModel = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(text):
    return embeddingsModel.encode(text, convert_to_numpy=True)


def add_to_memory(text, metadata=None, uid=None):
    embedding = embed_text(text)
    collection.add(
        embeddings=[embedding],
        documents=[text],
        metadatas=[metadata or {}],
        ids=[uid or str(hash(text))],
    )


def search_memory(query, top_k=3, max_distance=1):
    embedding = embed_text(query)
    result = collection.query(query_embeddings=[embedding], n_results=top_k)

    documents = result.get("documents", [[]])[0]
    distances = result.get("distances", [[]])[0]

    filtered = [doc for doc, dist in zip(documents, distances) if dist <= max_distance]

    return filtered
