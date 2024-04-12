import os
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

def render_template(data: dict) -> str:
    try:
        loader = FileSystemLoader('templates')
        env = Environment(loader=loader)
        template = env.get_template('invoice_template_claud_twocolumns_initial2.html')

        # Construct absolute path for the logo
        base_path = os.path.dirname(__file__)  # gets the directory in which this script is located
        logo_path = os.path.join(base_path, '..', 'templates/images/logo.png')
        data['logo_path'] = f'file://{logo_path}'  # add the logo path to the data dictionary

        return template.render(**data)
    except Exception as e:
        print(f"Error rendering template: {e}")
        return ""

def generate_pdf(html: str) -> bytes:
    try:
        return HTML(string=html).write_pdf()
    except Exception as e:
        print(f"Error generating PDF:{e}")
        return b""

def generate_pdf_invoice(data: dict) -> bytes:
    invoice_number = data.get('invoice_number', f'invoice_{datetime.now().strftime("%Y%m%d%H%M%S")}')
    outputFileName = f'{invoice_number}.pdf'
    html = render_template(data)
    pdf = generate_pdf(html)
    with open(outputFileName, 'wb') as pdf_file:
        pdf_file.write(pdf)
    return pdf
