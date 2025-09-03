import wikipedia

def get_summary(topic: str) -> str:
    return wikipedia.summary(topic, sentences=3)
