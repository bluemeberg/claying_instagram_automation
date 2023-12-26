from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from starlette.config import Config
import httpx

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="!secret")

# 환경변수 또는 하드코딩된 값을 사용하여 구성
config = Config(".env")  # .env 파일에서 구성을 로드합니다.
FACEBOOK_CLIENT_ID = config("FACEBOOK_CLIENT_ID", cast=str, default="YOUR_FACEBOOK_CLIENT_ID")
FACEBOOK_CLIENT_SECRET = config("FACEBOOK_CLIENT_SECRET", cast=str, default="YOUR_FACEBOOK_CLIENT_SECRET")
print(FACEBOOK_CLIENT_ID)
REDIRECT_URI = "http://localhost:8000/callback"

@app.get("/login")
async def login(request: Request):
    request.session['oauth_state'] = "!state"  # 간단한 상태 값
    return RedirectResponse(
        url=f"https://www.facebook.com/v2.10/dialog/oauth?client_id={FACEBOOK_CLIENT_ID}&redirect_uri={REDIRECT_URI}&state={request.session['oauth_state']}&scope=email"
    )

@app.get("/callback")
async def callback(request: Request, state: str = "", code: str = ""):
    if state != request.session.get("oauth_state"):
        raise HTTPException(status_code=400, detail="State mismatch")

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://graph.facebook.com/v2.10/oauth/access_token",
            params={
                "client_id": FACEBOOK_CLIENT_ID,
                "client_secret": FACEBOOK_CLIENT_SECRET,
                "redirect_uri": REDIRECT_URI,
                "code": code,
            },
        )
        result = response.json()
        access_token = result.get("access_token")

        user_response = await client.get(f"https://graph.facebook.com/me?fields=id,name,email&access_token={access_token}")
        user_info = user_response.json()

    return user_info

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)