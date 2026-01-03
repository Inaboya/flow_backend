import difflib
from datetime import datetime

def calculate_score(inv_amt: float, tx_amt: float, inv_date: datetime, tx_date: datetime, inv_desc: str, tx_desc: str) -> tuple[float, str]:
    score = 0.0
    reasons = []

    # 1. Amount Match (Max 0.7)
    diff = abs(float(inv_amt) - float(tx_amt))
    if diff == 0:
        score += 0.7
        reasons.append("Exact amount match.")
    elif diff <= (float(inv_amt) * 0.02): # 2% tolerance
        score += 0.4
        reasons.append("Amount match within 2% tolerance.")

    # 2. Date Proximity (Max 0.2)
    days_diff = abs((inv_date - tx_date).days)
    if days_diff <= 2:
        score += 0.2
        reasons.append(f"Date proximity is high ({days_diff} days).")
    elif days_diff <= 7:
        score += 0.1
        reasons.append("Date is within a one-week window.")

    # 3. Text Similarity (Max 0.1)
    # Using SequenceMatcher for fuzzy string matching
    ratio = difflib.SequenceMatcher(None, inv_desc.lower(), tx_desc.lower()).ratio()
    if ratio > 0.8:
        score += 0.1
        reasons.append("Description strings are highly similar.")

    return min(score, 1.0), " ".join(reasons)