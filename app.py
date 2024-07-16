import streamlit as st
import fitz  # PyMuPDF
from io import BytesIO

def display_pdf(file_path, page_num, title="PDF Content"):
    st.subheader(title)
    # Open the PDF file
    doc = fitz.open(file_path)
    
    if 0 <= page_num < len(doc):
        page = doc.load_page(page_num)
        image = page.get_pixmap()
        
        # Convert to bytes
        img_bytes = image.tobytes()
        img = BytesIO(img_bytes)
        
        st.image(img, caption=f'Page {page_num + 1}', use_column_width=True)
    else:
        st.error("Page number out of range")

def main():
    st.title("PDF Viewer and PBIX Downloader")

    # Initialize session state for page navigation
    if "page_num" not in st.session_state:
        st.session_state.page_num = 0
    
    # Display contents of report.pdf with navigation
    num_pages = fitz.open("report.pdf").page_count
    display_pdf("report.pdf", st.session_state.page_num, "Contents of report.pdf")
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("Previous Page"):
            st.session_state.page_num = (st.session_state.page_num - 1) % num_pages
    with col3:
        if st.button("Next Page"):
            st.session_state.page_num = (st.session_state.page_num + 1) % num_pages
    
    # PBIX download button
    pbix_file_path = "dashboard.pbix"  # Replace with your .pbix file path
    with open(pbix_file_path, "rb") as file:
        pbix_bytes = file.read()
    st.download_button(
        label="Download .pbix file",
        data=pbix_bytes,
        file_name="report.pbix",
        mime="application/octet-stream"
    )

if __name__ == "__main__":
    main()
