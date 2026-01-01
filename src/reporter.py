def assess_risk(polarity_flip_rate):
    if polarity_flip_rate > 0:
        return "UNSAFE", ["POLARITY_FLIP"]
    return "SAFE", []
# def assess_drift(bucket_drift_rate):
#     if bucket_drift_rate > 0.1:
#         return "UNSAFE", ["BUCKET_DRIFT"]
#     return "SAFE", []