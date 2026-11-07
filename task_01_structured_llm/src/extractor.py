import os
from google.genai import types
from pydantic import ValidationError

from task_01_structured_llm.src.llm_client import get_genai_client
from task_01_structured_llm.src.prompt_builder import build_extraction_prompt
from task_01_structured_llm.src.schemas import InvoiceData


class InvoiceExtractor:
    def __init__(self, model_name: str = None):
        self.client = get_genai_client()
        self.model_name = model_name or os.getenv(
            "GEMINI_MODEL", "gemini-2.5-flash"
        )
        # Chỉ dùng các model chắc chắn hỗ trợ trong API Key của bạn
        self.fallback_models = [
            "gemini-2.5-flash",
            "gemini-2.5-pro",
            "gemini-2.5-flash-lite",
            "gemini-3.5-flash",
        ]

    def extract(self, raw_text: str) -> InvoiceData:
        if not raw_text or not isinstance(raw_text, str) or not raw_text.strip():
            raise ValueError("Input raw_text cannot be empty or non-string.")

        prompt = build_extraction_prompt(raw_text, doc_type="invoice")

        config = types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=InvoiceData,
            temperature=0.1,
        )

        models_to_try = [self.model_name] + [
            m for m in self.fallback_models if m != self.model_name
        ]

        last_exception = None
        response = None

        for model in models_to_try:
            try:
                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config=config,
                )
                if response and response.text:
                    break
            except Exception as e:
                last_exception = e
                continue

        if not response or not response.text:
            raise RuntimeError(
                f"Gemini API request failed across all candidate models. Last error: {last_exception}"
            ) from last_exception

        try:
            return InvoiceData.model_validate_json(response.text)
        except ValidationError as e:
            raise RuntimeError(
                f"JSON response failed Pydantic validation: {e}"
            ) from e