from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()


@router.get("/")
def example():
    return {
        "ok": True
    }
