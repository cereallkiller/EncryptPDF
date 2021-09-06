import PyPDF2


def secure_pdf(pdf_file, pdf_password):
    parser = PyPDF2.PdfFileWriter()
    pdf = PyPDF2.PdfFileReader(pdf_file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(pdf_password)
    with open(f"encrypted_{pdf_file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"Secure PDF encrypted_{pdf_file} are created")


if __name__ == "main":
    file = "pdf_file_name.pdf"
    password = "my_strong_password"
    secure_pdf(file, password)
