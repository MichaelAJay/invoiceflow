from typing import List
from pydantic import BaseModel

class InvoiceItem(BaseModel):
    name: str
    description: str
    quantity: int
    amount: float
    price: str

class InvoiceBill(BaseModel):
    name: str
    value: float

class InvoiceData(BaseModel):
    company_name: str
    company_address: str
    company_contact: str
    company_logo: str
    customer_name: str
    customer_company: str
    customer_address: str
    customer_contact: str
    invoice_number: str
    invoice_date: str
    order_date: str
    due_date: str
    payment_terms: str
    invoice_items: List[InvoiceItem]
    invoice_bills: List[InvoiceBill]
    total_amount: float
    notes: str
    subtotal: str
    tax: str
    delivery_fee: str
    tip: str
    discounts_fees: str
    total: str
    company_address_str: str
    company_address_city_st_zip: str
    company_phone: str