from fastapi import Header, HTTPException


def api_key_auth(x_api_key: str | None = Header(default=None)):
    if x_api_key is None:
        raise HTTPException(status_code=401, detail="API Key ausente.")
    return x_api_key
