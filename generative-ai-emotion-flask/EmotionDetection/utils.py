def map_label_to_emotion(label):
    emotions = ["anger", "fear", "joy", "love", "sadness", "surprise"]
    return emotions[label] if label < len(emotions) else "unknown"
