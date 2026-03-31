import streamlit as st
import os

from src.parser import extract_text
from src.inspection_extractor import extract_inspection_data
from src.thermal_extractor import extract_thermal_data
from src.merger import merge_data
from src.ddr_generator import generate_ddr
from src.report_builder import create_pdf

st.title("🧠 AI DDR Report Generator")

inspection_file = st.file_uploader("Upload Inspection Report (PDF)", type=["pdf"])
thermal_file = st.file_uploader("Upload Thermal Report (PDF)", type=["pdf"])

if st.button("Generate Report"):

    if inspection_file and thermal_file:

        os.makedirs("outputs", exist_ok=True)

        # Save files
        with open("inspection.pdf", "wb") as f:
            f.write(inspection_file.read())

        with open("thermal.pdf", "wb") as f:
            f.write(thermal_file.read())

        st.info("⏳ Processing...")

        # Pipeline
        inspection_text = extract_text("inspection.pdf")
        thermal_text = extract_text("thermal.pdf")

        inspection_data = extract_inspection_data(inspection_text)
        thermal_data = extract_thermal_data(thermal_text)

        merged = merge_data(inspection_data, thermal_data)

        # Generate clean DDR text
        ddr = generate_ddr(merged, [])

        # Create PDF
        create_pdf(ddr)

        st.success("✅ DDR Report Generated!")

        # ✅ ONLY SHOW THIS
        st.subheader("🧾 DDR Report")
        st.text(ddr)

        st.info("📁 PDF saved in outputs/ddr_report.pdf")

    else:
        st.warning("⚠️ Please upload both files!")