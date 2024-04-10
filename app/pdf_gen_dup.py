from .models import InvoiceData
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

def render_template(data: InvoiceData) -> str:
    try:
        # Import an HTML template
        loader = FileSystemLoader('templates')
        env = Environment(loader=loader)
        template = env.get_template('invoice_template.html')
        return template.render(**data.model_dump())
    except Exception as e:
        print(f"Error rendering template: {e}")
        return ""
    
def generate_pdf(html: str) -> bytes:
    try:
        return HTML(string=html).write_pdf()
    except Exception as e:
        print(f"Error generating PDF:{e}")
        return b""

def generate_pdf_invoice(data: InvoiceData, outputFileName: str) -> bytes:
    html = render_template(data)

    # Use WeasyPrint to generate the PDF
    pdf = generate_pdf(html)

    # Write the pdf make sure 'wb'
    with open(outputFileName, 'wb') as pdf_file:
        pdf_file.write(pdf)

    # Return the pdf
    return pdf
