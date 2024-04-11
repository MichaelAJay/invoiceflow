from typing import List
from pydantic import BaseModel

class InvoiceItem(BaseModel):
    name: str
    description: str
    quantity: int
    amount: float

class InvoiceBill(BaseModel):
    name: str
    value: float

class InvoiceData(BaseModel):
    company_name: str
    company_address: str
    company_contact: str
    company_logo: str
    customer_name: str
    customer_address: str
    customer_contact: str
    invoice_number: str
    invoice_date: str
    payment_terms: str
    invoice_items: List[InvoiceItem]
    invoice_bills: List[InvoiceBill]
    total_amount: float
    notes: str