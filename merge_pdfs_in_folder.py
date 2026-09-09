from pathlib import Path
from pypdf import PdfWriter

# Folder containing the PDFs
folder = Path(r"C:\Users\kupfe\Downloads\2025")

# Output PDF
output_file = folder / "merged.pdf"

# Get PDFs and sort lexicographically by filename
pdf_files = sorted(folder.glob("*.pdf"), key=lambda p: p.name)

# Exclude the output file if it already exists
pdf_files = [p for p in pdf_files if p != output_file]

writer = PdfWriter()

for pdf_file in pdf_files:
    print(f"Adding: {pdf_file.name}")
    writer.append(str(pdf_file))

with open(output_file, "wb") as f:
    writer.write(f)

print(f"\nMerged {len(pdf_files)} PDFs into:")
print(output_file)