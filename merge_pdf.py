from pypdf import PdfReader, PdfWriter


def merge_pdf_page_ranges(pdf_paths, page_ranges, output_pdf):
    """
    Parameters
    ----------
    pdf_paths : list[str]
        List of input PDF paths.

    page_ranges : list[list[int]] or list[tuple[int, int]]
        List of [start_page, end_page] pairs.
        Pages are 1-based and inclusive.

    output_pdf : str
        Output PDF path.
    """

    if len(pdf_paths) != len(page_ranges):
        raise ValueError("pdf_paths and page_ranges must have the same length")

    writer = PdfWriter()

    for pdf_path, (start_page, end_page) in zip(pdf_paths, page_ranges):
        reader = PdfReader(pdf_path)

        num_pages = len(reader.pages)

        if start_page < 1 or end_page > num_pages or start_page > end_page:
            raise ValueError(
                f"Invalid page range [{start_page}, {end_page}] "
                f"for file {pdf_path} with {num_pages} pages"
            )

        # Convert from 1-based page numbering to 0-based indexing
        for page_idx in range(start_page - 1, end_page):
            writer.add_page(reader.pages[page_idx])

    with open(output_pdf, "wb") as f:
        writer.write(f)
        
pdf_files = [
    r"C:\Users\Beer8416\Downloads\krina\krina_2025.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2006.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2007.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2008.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2009.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2010.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2011.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2012.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2013_1.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2013_2.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2014_1.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2014_2.pdf",    
r"C:\Users\Beer8416\Downloads\krina\krina_2015_1.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2015_2.pdf",    
r"C:\Users\Beer8416\Downloads\krina\krina_2016_1.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2016_2.pdf",    
r"C:\Users\Beer8416\Downloads\krina\krina_2017_1.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2017_2.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2018_1.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2018_2.pdf",  
r"C:\Users\Beer8416\Downloads\krina\krina_2019.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2020.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2021.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2022.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2023.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2024.pdf",
r"C:\Users\Beer8416\Downloads\krina\krina_2025.pdf",
r"C:\Users\Beer8416\Downloads\krina\formulas.pdf"
]

page_ranges = [
    [1,1],#"C:\Users\Beer8416\Downloads\krina\krina_2025.pdf",
    [2,12],#"C:\Users\Beer8416\Downloads\krina\krina_2006.pdf",
[2,8],#"C:\Users\Beer8416\Downloads\krina\krina_2007.pdf",
[2,8],#"C:\Users\Beer8416\Downloads\krina\krina_2008.pdf",
[2,8],#"C:\Users\Beer8416\Downloads\krina\krina_2009.pdf",
[2,11],#"C:\Users\Beer8416\Downloads\krina\krina_2010.pdf",
[2,7],#"C:\Users\Beer8416\Downloads\krina\krina_2011.pdf",
[2,6],#"C:\Users\Beer8416\Downloads\krina\krina_2012.pdf",
[2,6],#"C:\Users\Beer8416\Downloads\krina\krina_2013_1.pdf",
[7,9],#"C:\Users\Beer8416\Downloads\krina\krina_2013_2.pdf",    
[2,8],#"C:\Users\Beer8416\Downloads\krina\krina_2014_1.pdf",
[7,9],#"C:\Users\Beer8416\Downloads\krina\krina_2014_2.pdf",    
[2,6],#"C:\Users\Beer8416\Downloads\krina\krina_2015_1.pdf",
[7,9],#"C:\Users\Beer8416\Downloads\krina\krina_2015_2.pdf",    
[2,9],#"C:\Users\Beer8416\Downloads\krina\krina_2016_1.pdf",
[8,11],#"C:\Users\Beer8416\Downloads\krina\krina_2016_2.pdf",    
[2,10],#"C:\Users\Beer8416\Downloads\krina\krina_2017_1.pdf",
[11,13],#"C:\Users\Beer8416\Downloads\krina\krina_2017_2.pdf",
[2,6],#"C:\Users\Beer8416\Downloads\krina\krina_2018_1.pdf",
[8,10],#"C:\Users\Beer8416\Downloads\krina\krina_2018_2.pdf",
[2,9],#"C:\Users\Beer8416\Downloads\krina\krina_2019.pdf",
[2,9],#"C:\Users\Beer8416\Downloads\krina\krina_2020.pdf",
[2,7],#"C:\Users\Beer8416\Downloads\krina\krina_2021.pdf",
[2,9],#"C:\Users\Beer8416\Downloads\krina\krina_2022.pdf",
[2,7],#"C:\Users\Beer8416\Downloads\krina\krina_2023.pdf",
[2,8],#"C:\Users\Beer8416\Downloads\krina\krina_2024.pdf",
[2,7],#"C:\Users\Beer8416\Downloads\krina\krina_2025.pdf",
[1,8],#"C:\Users\Beer8416\Downloads\krina\formulas.pdf"
]

merge_pdf_page_ranges(
    pdf_files,
    page_ranges,
    "krina_merged.pdf"
)
num_pages = 0
for l in page_ranges:
    num_pages+=(l[1]-l[0]+1)
print(    num_pages)
    
