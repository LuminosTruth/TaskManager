from fastapi import APIRouter, BackgroundTasks, Depends

from src.auth.base_config import current_user

from .tasks import send_email_report_dashboard

router = APIRouter(prefix="/report")


@router.get("/dashboard")
def get_dashboard_report():
    send_email_report_dashboard.delay("string")
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }
