from pydantic import BaseModel

class ScheduleInterface(BaseModel):
    cron_expression: str
    enabled: bool
    arguments: dict

class SchedulePatchInterface(BaseModel):
    enabled: bool| None
    arguments: dict | None