from .models import InvoiceData
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader


def generate_pdf_invoice(data: InvoiceData) -> bytes:
    # Import an HTML template
    loader = FileSystemLoader('templates')
    env = Environment(loader=loader)
    template = env.get_template('invoice-template.html')

    # Render the template with the data
    html = template.render(**data.model_dump())

    # Write the html
    with open('rendered_template.html', 'w') as f:
        f.write(html)

    # Use WeasyPrint to generate the PDF
    pdf = HTML(string=html).write_pdf()

    # Write the pdf
    with open('output.pdf', 'w') as f2:
        f2.write(pdf)

    # Return the pdf
    return pdf
