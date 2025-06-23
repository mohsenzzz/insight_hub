from pydantic import BaseModel

class ScheduleInterface(BaseModel):
    cron_expression: str
    enabled: bool
    arguments: dict