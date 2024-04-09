from .models import InvoiceData
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

TEMPLATE_FILE = 'templates/invoice_template.html' # Expecting this to not work
OUTPUT_HTML_FILE = 'rendered_template.html'
OUTPUT_PDF_FILE = 'output.pdf'

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

def generate_pdf_invoice(data: InvoiceData) -> bytes:
    html = render_template(data)

    # Write the html
    with open(OUTPUT_HTML_FILE, 'w') as html_file:
        html_file.write(html)

    # Use WeasyPrint to generate the PDF
    pdf = generate_pdf(html)

    # Write the pdf make sure 'wb'
    with open(OUTPUT_PDF_FILE, 'wb') as pdf_file:
        pdf_file.write(pdf)

    # Return the pdf
    return pdf
