def get_severity(item):
    if item.get("temperature"):
        temp = item["temperature"]

        if temp > 28:
            return "High"
        elif temp > 26:
            return "Medium"
        else:
            return "Low"

    if "leakage" in item["issue"]:
        return "High"

    if "crack" in item["issue"]:
        return "Medium"

    return "Low"