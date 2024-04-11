from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

def render_template(data: dict) -> str:
    try:
        loader = FileSystemLoader('templates')
        env = Environment(loader=loader)
        template = env.get_template('invoice_template_h4h.html')
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
