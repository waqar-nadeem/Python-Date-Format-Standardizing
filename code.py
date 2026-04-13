from datetime import datetime

def standardize_date(date_str):
    formats = ["%d-%m-%Y", "%m/%d/%Y", "%Y.%m.%d", "%Y/%m/%d", "%d %b %Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None

dates = ["12-04-2026", "04/12/2026", "2026.04.12", "2026/04/12", "12 Apr 2026"]
standardized = [standardize_date(d) for d in dates]
print(standardized)
