# Safe Binance Proxy (Starter Edition)

A lightweight FastAPI intent proxy designed to protect trading scripts, wrap Binance API endpoints, enforce order risk limits, and block unauthorized capital withdrawals.

## 🛡️ Why Use an Intent Proxy?
Exposed API keys and misconfigured trading algorithms carry major structural risks. This proxy sits directly between your trading client and the Binance API, evaluating risk guardrails before requests reach the exchange.

## Starter Features
- 🔒 **Token Authentication:** Enforces security headers on incoming proxy traffic.
- 🛑 **Withdrawal Interceptor:** Automatically blocks endpoints like `/sapi/v1/capital/withdraw/apply` with a `403 Forbidden` response.
- 📊 **Order Quantity Guard:** Prevents oversized trade execution beyond pre-set thresholds.

---

### ⚡ Upgrade to the Full MVP Build
Get the complete production-ready source code—including the **Programmatic Circuit Breaker**, **Async HTTPX Routing**, and **Pydantic Data Models**:

👉 **[Download Safe Binance Proxy MVP on Gumroad](https://dynamo3860.gumroad.com/l/wpwgmf)**

---

## Quickstart Code (`main.py`)

```python
from fastapi import FastAPI, HTTPException, Request, status

app = FastAPI(title="Safe Binance Proxy Starter")

BLOCKED_ROUTES = ["/sapi/v1/capital/withdraw"]

@app.get("/health")
def health():
    return {"status": "active", "mode": "starter"}

@app.api_route("/proxy/{path:path}", methods=["GET", "POST"])
async def route_proxy(path: str, request: Request):
    for blocked in BLOCKED_ROUTES:
        if blocked in path:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Blocked: Intent Firewall intercepted withdrawal route."
            )
    return {"message": "Endpoint cleared firewall. Connect your exchange client here."}
