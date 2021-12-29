from datetime import datetime
from enum import Enum
from typing import Dict, Literal, Optional, Union

from pydantic import BaseModel, root_validator


class PlatformName(str, Enum):
    KAKAO = 'KAKAO'


class PlatformContext(BaseModel):
    cellphone: Optional[str]


class Platform(BaseModel):
    name: PlatformName
    context: PlatformContext


class Metadata(BaseModel):
    mall_hash_id: str


class ScheduleType(str, Enum):
    TARGET = 'TARGET'
    RANGE = 'RANGE'


class TargetSchedule(BaseModel):
    type: Literal[ScheduleType.TARGET]
    send_time: datetime


class RangeSchedule(BaseModel):
    type: Literal[ScheduleType.RANGE]
    send_start_time: datetime
    send_end_time: datetime

    @root_validator
    def validate_time(cls, values):
        validated_send_start_time: datetime = values.get('send_start_time')
        validated_send_end_time: datetime = values.get('send_end_time')
        if validated_send_start_time >= validated_send_end_time:
            raise ValueError('`start_end_time` should be later than `start_start_time.')
        return values


class Message(BaseModel):
    platform: Platform
    metadata: Dict[str, Union[str, list]]
    schedule: Union[TargetSchedule, RangeSchedule]
    payload: Union[dict, str]
