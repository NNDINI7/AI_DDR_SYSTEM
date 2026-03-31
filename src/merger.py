def merge_data(inspection, thermal):
    merged = []
    seen = set()

    for item in inspection + thermal:
        key = (item["area"], item["issue"])

        if key not in seen:
            seen.add(key)
            merged.append(item)

    return merged