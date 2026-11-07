# Create template prompt with parameterized prompt and role prompt
def build_extraction_prompt(
        unstructured_text: str, doc_type: str = "invoice"
)-> str:
    if not unstructured_text or not unstructured_text.strip():
        raise Exception("Please provide text")
    prompt = f"""You are an expert data extraction assistant specializing in analyzing raw text documents.

    Your objective: Extract key information from the provided {doc_type} text accurately.

    Rules:
    1. Preserve numbers, dates, and names exactly as stated in the text.
    2. If a specific field is not explicitly mentioned, assign a logical default or leave it empty according to the target schema.
    3. Strictly format the output as JSON according to the requested schema. Do not add conversational text or markdown wrappers outside the JSON response.

    Input {doc_type.capitalize()} Text:
    ---
    {unstructured_text.strip()}
    ---
    """

    return prompt