from typing import List
from pydantic import BaseModel

class InvoiceData(BaseModel):
    from_name: str
    to_name: str
    date: str
    line_items: List[dict]
    subtotal: float
    tax_items: List[dict]
    total: float