def agreement_rate(clusters, total_items):
    return len(clusters) / total_items

def polarity_flip_rate(clusters):
    flips = 0
    for c in clusters:
        polarities = {i["polarity"] for i in c["items"]}
        if len(polarities) > 1:
            flips += 1
    return flips / len(clusters)

def bucket_drift_rate(clusters):
    drift = 0
    for c in clusters:
        buckets = set()
        for i in c["items"]:
            if "intensity_bucket" in i:
                buckets.add(i["intensity_bucket"])
        if len(buckets) > 1:
            drift += 1
    return drift / len(clusters)
