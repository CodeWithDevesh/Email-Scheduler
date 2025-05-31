from fastapi import APIRouter, Depends
from app.database import get_db_async
from app.models.email_tasks import EmailTasks
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.email_task import EmailTaskCreate, EmailTaskResponse


router = APIRouter(prefix="/scheduler", tags=["Scheduler"])


@router.post("/", response_model=EmailTaskResponse)
async def create_email_task(
    email_task: EmailTaskCreate, db: AsyncSession = Depends(get_db_async)
):
    """
    Create a new email task to be scheduled.
    """
    email_task_dict = email_task.model_dump()
    new_task = EmailTasks(**email_task_dict)
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task
