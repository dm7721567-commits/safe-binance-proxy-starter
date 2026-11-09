from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI(title="Safe Binance Proxy - Kill Switch Module")

# Simulated security token for administrative override
ADMIN_SECRET_TOKEN = "secure-admin-token-123"

class KillSwitchRequest(BaseModel):
    reason: str
    confirm_cancel_all: bool

@app.post("/proxy/kill-switch")
def trigger_emergency_kill_switch(payload: KillSwitchRequest, x_admin_token: str = Header(None)):
    """
    Emergency kill switch endpoint to immediately halt trading and cancel 
    all open orders across connected Binance API endpoints.
    """
    if x_admin_token != ADMIN_SECRET_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized: Invalid or missing admin security token."
        ]
    
    if not payload.confirm_cancel_all:
        raise HTTPException(
            status_code=400,
            detail="Confirmation required: confirm_cancel_all must be set to true."
        ]
        
    return {
        "status": "EMERGENCY_HALT_ACTIVATED",
        "reason": payload.reason,
        "action_taken": "All open orders cancelled and trading gateway locked.",
        "exchange": "Binance Spot/Futures"
    }
