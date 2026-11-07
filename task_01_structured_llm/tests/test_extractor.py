import pytest
from task_01_structured_llm.src.extractor import InvoiceExtractor
from task_01_structured_llm.src.schemas import InvoiceData


def test_invoice_extractor_integration():
    """Test happy path: valid input text should return correctly parsed InvoiceData."""
    sample_text = """
    INVOICE #INV-101
    Date: 2026-10-10
    Vendor: Acme Supplies
    Customer: John Doe
    Items:
    - Office Chair, Qty: 1, Price: $120.00, Total: $120.00
    Subtotal: $120.00
    Tax: $12.00
    Total: $132.00
    Currency: USD
    """
    extractor = InvoiceExtractor()
    result = extractor.extract(sample_text)

    # Validate output type
    assert isinstance(result, InvoiceData)

    # Validate specific extracted fields
    assert result.invoice_number == "INV-101"
    assert result.vendor_name == "Acme Supplies"
    assert result.total_amount == 132.00

    # Validate nested items
    assert len(result.items) == 1
    assert result.items[0].quantity == 1


def test_empty_input_raises_error():
    """Test edge case: empty or whitespace input should raise ValueError."""
    extractor = InvoiceExtractor()

    with pytest.raises(ValueError, match="Input raw_text cannot be empty"):
        extractor.extract("")

    with pytest.raises(ValueError):
        extractor.extract("   \n  ")