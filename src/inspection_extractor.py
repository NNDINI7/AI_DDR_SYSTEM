def extract_inspection_data(text):
    data = []

    issues_map = [
        ("Hall", "dampness"),
        ("Bedroom", "dampness"),
        ("Master Bedroom", "dampness"),
        ("Kitchen", "dampness"),
        ("Parking", "leakage"),
        ("Common Bathroom", "tile joint gaps"),
        ("External Wall", "cracks"),
    ]

    for area, issue in issues_map:
        if area.lower() in text.lower():
            data.append({
                "area": area,
                "issue": issue,
                "source": "inspection"
            })

    return data