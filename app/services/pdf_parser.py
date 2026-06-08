from io import BytesIO
import pdfplumber
from fastapi import UploadFile, HTTPException
from app.utils.text_cleaner import clean_text


async def extract_text_from_pdf(file: UploadFile) -> str:
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Envie um arquivo PDF válido.")

    content = await file.read()

    try:
        with pdfplumber.open(BytesIO(content)) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Não foi possível ler o PDF.") from exc

    text = clean_text(text)
    if not text:
        raise HTTPException(status_code=400, detail="PDF sem texto extraível.")

    return text
