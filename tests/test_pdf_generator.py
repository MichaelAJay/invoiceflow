import unittest
from app.pdf_generator import render_template, generate_pdf, generate_pdf_invoice
from app.models import InvoiceData

class TestFunctions(unittest.TestCase):
    
    def test_render_template(self):
        data = InvoiceData({
            "from_name": "John Doe",
            "to_name": "Jane Doe",
            "date": "2022-01-01",
            "line_items": [
                {"name": "Item 1", "quantity": 2, "price": 10.99},
                {"name": "Item 2", "quantity": 3, "price": 9.99}
            ],
            "subtotal": 31.97,
            "tax_items": [
                {"name": "Tax 1", "amount": 2.00},
                {"name": "Tax 2", "amount": 1.50}
            ],
            "total": 35.47
        })
        html = render_template(data)
        self.assertIsNotNone(html)
    
    def test_generate_pdf(self):
        html = 'Test PDF'
        pdf = generate_pdf(html)
        self.assertIsNotNone(pdf)
        self.assertIsInstance(pdf, bytes)

if __name__=='__main__':
    unittest.main()