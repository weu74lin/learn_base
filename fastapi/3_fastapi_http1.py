"""
浏览器两步：
  1) 打开页面  /agent_step/        → HTML（常有重定向，学习阶段可跳过）
  2) 筛选查询  /agent_step/query   → JSON（真正要的数据）

用代码取数：只做第 2 步即可。
"""

from fastapi import FastAPI, HTTPException, Query
import httpx

app = FastAPI()

QUERY_URL = "https://service.maituai.com/live-interact/agent_step/query"


@app.get("/query_agent")
async def query_agent(
    query_id: str = Query(..., description="筛选：query_id"),
    reply_type: str = Query(..., description="筛选：reply_type，如 my_twins"),
):
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            r = await client.get(
                QUERY_URL,
                params={
                    "query_id": query_id,
                    "reply_type": reply_type,
                },
            )
            r.raise_for_status()
            data = r.json()
    except httpx.HTTPError as e:
        # 把真实原因返回到 docs，避免只看到笼统的 Internal Server Error
        raise HTTPException(status_code=502, detail=f"请求外部接口失败: {e}") from e

    return {"query_result": data}
