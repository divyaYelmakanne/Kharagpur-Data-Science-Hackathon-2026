import os

def load_data(data_path):
    samples = []
    for file in os.listdir(data_path):
        if file.endswith(".txt"):
            story_id = file.split(".")[0]
            with open(os.path.join(data_path, file), "r", encoding="utf-8") as f:
                narrative = f.read()

            with open(os.path.join(data_path, story_id + "_backstory.txt")) as b:
                backstory = b.read()

            samples.append((story_id, narrative, backstory))
    return samples
