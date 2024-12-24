from fastapi import FASTAPI

app = FASTAPI()

@app.get("/ping")
async def ping():
    return "Hello i am alive"



