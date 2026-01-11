from data_loader import load_data
from retriever import retrieve_evidence
from reasoning import judge_consistency
import pandas as pd

def main():
    data = load_data("data/")
    results = []

    for story_id, narrative, backstory in data:
        evidence = retrieve_evidence(narrative, backstory)
        prediction, rationale = judge_consistency(evidence, backstory)

        results.append({
            "story_id": story_id,
            "prediction": prediction,
            "rationale": rationale
        })

    df = pd.DataFrame(results)
    df.to_csv("results.csv", index=False)

if __name__ == "__main__":
    main()
