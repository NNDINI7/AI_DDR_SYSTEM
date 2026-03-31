from src.severity import get_severity

def generate_ddr(merged, images=None):
    if images is None:
        images = []

    report = "DAMAGE DIAGNOSTIC REPORT (DDR)\n"
    report += "=" * 40 + "\n\n"

    for i, item in enumerate(merged):
        report += f"{i+1}. Area: {item['area']}\n"
        report += f"   Issue: {item['issue']}\n"
        report += f"   Severity: {item.get('severity', 'Low')}\n"
        report += f"   Image: {item.get('image', 'Not Available')}\n"
        report += "-" * 30 + "\n"

    return report