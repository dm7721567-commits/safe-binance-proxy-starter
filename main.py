from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI(
    title="Safe Binance Proxy Starter",
    description="Intent firewall to intercept and block unauthorized Binance API withdrawals.",
    version="1.0.0"
)

class OrderRequest(BaseModel):
    symbol: str
    side: str
    quantity: float
    price: float

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "Safe Binance Proxy Intent Firewall",
        "gumroad_mvp": "https://dynamo3860.gumroad.com/l/wpwgmf"
    }

@app.post("/proxy/order")
def create_guarded_order(order: OrderRequest):
    # Intent firewall rule: Block oversized quantities as a basic circuit breaker
    MAX_ALLOWED_QUANTITY = 10.0
    if order.quantity > MAX_ALLOWED_QUANTITY:
        raise HTTPException(
            status_code=403,
            detail=f"Blocked by Safe Binance Proxy: Order quantity {order.quantity} exceeds safety threshold ({MAX_ALLOWED_QUANTITY})."
        ]
    
    return {
        "status": "success",
        "message": "Order passed safety guardrails and intent verification.",
        "order": order.dict()
    }

@app.post("/proxy/withdraw")
def block_unauthorized_withdrawal(request: Request):
    # Default intent firewall stance: Block all direct external withdrawals via starter proxy
    raise HTTPException(
        status_code=403,
        detail="Security Alert: Direct API withdrawals are strictly blocked by Safe Binance Proxy."
    )
