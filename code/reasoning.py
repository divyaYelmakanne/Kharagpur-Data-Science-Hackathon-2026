def judge_consistency(evidence_chunks, backstory):
    contradiction_signals = 0

    for chunk in evidence_chunks:
        if "never" in chunk.lower() and "always" in backstory.lower():
            contradiction_signals += 1

    if contradiction_signals > 1:
        return 0, "Backstory contradicts multiple later narrative constraints"
    else:
        return 1, "Backstory aligns with observed character development"
