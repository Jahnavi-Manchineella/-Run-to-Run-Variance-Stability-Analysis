from load_data import load_runs
from matcher import match_items
from metrics import agreement_rate, polarity_flip_rate, bucket_drift_rate
from reporter import assess_risk
import json
from pathlib import Path

runs = load_runs()
print("Loaded journals:", len(runs))

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

report = []

for journal_id, journal_runs in runs.items():
    clusters = match_items(journal_runs)
    total_items = sum(len(r["items"]) for r in journal_runs)

    ar = agreement_rate(clusters, total_items)
    pfr = polarity_flip_rate(clusters)
    bdr = bucket_drift_rate(clusters)

    decision, flags = assess_risk(pfr)

    print("\n==============================")
    print(f"Journal ID: {journal_id}")
    print("==============================")
    print(f"Agreement Rate: {ar:.2f}")
    print(f"Polarity Flip Rate: {pfr:.2f}")
    print(f"Bucket Drift Rate: {bdr:.2f}")
    print(f"Decision: {decision}")
    print(f"Risk Flags: {flags}")

    report.append({
        "journal_id": journal_id,
        "agreement_rate": ar,
        "polarity_flip_rate": pfr,
        "bucket_drift_rate": bdr,
        "decision": decision,
        "risk_flags": flags
    })

with open(output_dir / "stability_report.json", "w") as f:
    json.dump(report, f, indent=2)
