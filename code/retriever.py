import pathway as pw

def retrieve_evidence(narrative, backstory):
    # Chunk narrative
    chunks = [narrative[i:i+2000] for i in range(0, len(narrative), 2000)]

    # Simple keyword overlap scoring (baseline)
    relevant_chunks = []
    for chunk in chunks:
        if any(word in chunk.lower() for word in backstory.lower().split()):
            relevant_chunks.append(chunk)

    return relevant_chunks[:10]
