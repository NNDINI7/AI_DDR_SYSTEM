# AI_DDR_SYSTEM
 Project Overview

This project is an end-to-end AI-based system designed to automatically generate a Damage Diagnostic Report (DDR) from two types of input documents:

Inspection Report
Thermal Report

In real-world scenarios, engineers manually analyze these reports to identify issues such as dampness, cracks, or leakage. This process is time-consuming and inconsistent.

This system automates that entire workflow by extracting useful information from the reports, combining it, and generating a clean, readable DDR output along with a PDF report.

🎯 Objective of the Project

The main goal of this project is to:

Reduce manual effort in analyzing reports
Convert unstructured PDF data into structured insights
Generate a clear and understandable diagnostic report
Build a system that mimics a real-world AI pipeline
⚙️ System Workflow (End-to-End Pipeline)

The system follows a structured pipeline:

Upload inspection and thermal reports
Extract text from PDFs
Identify important data (area and issue)
Merge both datasets
Generate DDR report
Display output in UI
Save final report as PDF

This modular flow makes the system easy to understand, debug, and improve.

🧠 Technologies Used and Why
Python

Python is used as the core language because it provides strong support for:

data processing
text handling
quick prototyping
Streamlit

Used for building the UI because:

very lightweight and simple
allows quick interaction
no need for frontend frameworks
pdfplumber

Used for extracting text from PDF files because:

works well with structured PDFs
easy to integrate
FPDF

Used to generate the final PDF report because:

simple and efficient
allows formatted text output
(Future Scope) OCR

OCR was considered as an enhancement to handle scanned PDFs where text extraction may fail.

📂 Project Structure and File Explanation

The project is designed in a modular way. Each file has a clear responsibility.

🔹 app.py (Main Entry Point)

This is the main file where the application starts.

What it does:

Creates the Streamlit UI
Takes user input (PDF upload)
Calls all backend modules in sequence
Displays the final DDR report
Triggers PDF generation

Why it is important:
This file connects the entire system and provides user interaction.

🔹 src/parser.py (Text Extraction Module)

What it does:

Reads PDF files
Extracts text content

Why it is needed:
PDF files contain raw data, and before processing anything, we need to convert them into readable text.

🔹 src/inspection_extractor.py

What it does:

Processes inspection report text
Extracts:
area (Hall, Kitchen, Bedroom, etc.)
issue (dampness, cracks, leakage)

Why it is needed:
Inspection reports are unstructured, so this module converts them into structured data.

🔹 src/thermal_extractor.py

What it does:

Processes thermal report text
Extracts relevant observations

Why it is needed:
Thermal reports provide additional insights, and this module ensures the system can handle multiple data sources.

🔹 src/merger.py

What it does:

Combines inspection and thermal data

Why it is needed:
Data from different sources must be unified into one structure before generating the final report.

🔹 src/ddr_generator.py

What it does:

Converts merged data into a clean, readable DDR format
Assigns severity levels (Low / High)

Why it is important:
This is the core logic that transforms raw structured data into meaningful insights.

🔹 src/report_builder.py

What it does:

Generates a PDF report from DDR text

Why it is needed:
Provides a real-world usable output that can be shared or stored.

🔹 outputs/

What it contains:

Final generated PDF report

Why it is needed:
Stores the output of the system.

🖥️ How to Run the Project
Install dependencies:
pip install -r requirements.txt
Run the application:
streamlit run app.py
Upload both reports and click "Generate Report"

📊 Output

The system provides:

Clean DDR text displayed in UI
PDF report saved in outputs folder

The output includes:

Area
Issue
Severity

⚠️ Limitations
Works best with structured or semi-structured PDFs
Extraction accuracy depends on report format
Severity logic is rule-based and can be improved

🚀 Future Improvements
Add OCR support for scanned PDFs
Use NLP models for better extraction
Improve severity prediction using ML
Enhance UI for better user experience

💡 Key Strengths of the Project
Complete end-to-end pipeline
Modular and scalable design
Converts raw data into actionable insights
Real-world use case implementation
Clean and user-friendly output

📌 Conclusion
This project demonstrates how AI and data processing techniques can be used to automate real-world workflows. It focuses not just on extracting data, but on transforming it into meaningful and usable information.
