def overlap(a, b):
    return a in b or b in a

def match_items(runs):
    clusters = []

    for run in runs:
        for item in run["items"]:
            matched = False
            for cluster in clusters:
                if (
                    item["domain"] == cluster["domain"]
                    and overlap(item["evidence_span"], cluster["evidence_span"])
                ):
                    cluster["items"].append(item)
                    matched = True
                    break
            if not matched:
                clusters.append({
                    "domain": item["domain"],
                    "evidence_span": item["evidence_span"],
                    "items": [item]
                })
    return clusters
