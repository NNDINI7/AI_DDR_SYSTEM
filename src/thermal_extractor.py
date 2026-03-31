import re

def extract_thermal_data(text):
    data = []

    hotspots = re.findall(r"Hotspot\s*:\s*(\d+\.?\d*)", text)

    for temp in hotspots:
        temp = float(temp)

        data.append({
            "area": "Unknown Area",
            "issue": "Thermal anomaly (possible moisture)",
            "temperature": temp,
            "source": "thermal"
        })

    return data