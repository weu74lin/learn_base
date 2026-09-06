from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/ip")
async def get_my_ip():
    # 你的服务主动去访问网上的接口
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/ip")
        r.raise_for_status()
        data = r.json()   # 网上返回的 JSON → Python dict
    return {"from_internet": data}