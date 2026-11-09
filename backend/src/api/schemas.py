"""Pydantic response schemas for OpenAPI spec generation.

These models define the structure of API responses so that FastAPI can generate
a complete OpenAPI specification with typed fields instead of generic object/any.
Each schema mirrors the output of an entity's to_dict() method.
"""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


# Team schemas
class TeamRecord(BaseModel):
    wins: int = 0
    losses: int = 0
    ties: int = 0
    count: int = 0
    winrate: float = 0.0


class TeamNormEpa(BaseModel):
    current: Optional[float] = None
    recent: Optional[float] = None
    mean: Optional[float] = None
    max: Optional[float] = None


class TeamResponse(BaseModel):
    team_number: int
    name: str
    nickname: Optional[str] = None
    city: Optional[str] = None
    state_prov: Optional[str] = None
    country: Optional[str] = None
    website: Optional[str] = None
    rookie_year: Optional[int] = None
    record: TeamRecord
    norm_epa: TeamNormEpa


# Event schemas
class EventMetrics(BaseModel):
    rp_pred: Optional[float] = None
    rp_3: Optional[float] = None


class EventResponse(BaseModel):
    event_key: str
    name: str
    short_name: Optional[str] = None
    city: Optional[str] = None
    state_prov: Optional[str] = None
    country: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    year: int
    event_type: Optional[int] = None
    webcast: Optional[List[Any]] = None
    metrics: EventMetrics


# Match schemas
class AlliancePred(BaseModel):
    pred: float = 0.0


class AllianceResult(BaseModel):
    score: int = 0


class AllianceResponse(BaseModel):
    team_keys: List[str]
    surrogate_team_keys: Optional[List[str]] = None
    dq_team_keys: Optional[List[str]] = None
    pred: Optional[AlliancePred] = None
    result: Optional[AllianceResult] = None


class MatchResponse(BaseModel):
    match_key: str
    event_key: str
    comp_level: str
    set_number: int
    match_number: int
    alliances: Dict[str, AllianceResponse]
    pre_epas: Optional[Dict[str, float]] = None
    epas: Optional[Dict[str, float]] = None
    time: Optional[float] = None
    actual_time: Optional[float] = None
    predicted_time: Optional[float] = None
    breakdown: Optional[Dict[str, Any]] = None


# TeamEvent schemas
class TeamEpaBreakdown(BaseModel):
    """Dynamic fields by year - use Dict to capture all keys."""
    pass


class TeamEpaStats(BaseModel):
    mean: float = 0.0
    std_dev: float = 0.0
    min: Optional[float] = None
    max: Optional[float] = None


class TeamEpaResponse(BaseModel):
    total_points: float = 0.0
    unitless: float = 0.0
    norm: float = 0.0
    breakdown: Dict[str, Optional[float]] = {}
    stats: TeamEpaStats


class TeamEventRecordSub(BaseModel):
    wins: int = 0
    losses: int = 0
    ties: int = 0
    count: int = 0
    winrate: float = 0.0


class TeamEventRecord(BaseModel):
    qual: TeamEventRecordSub
    elim: TeamEventRecordSub
    total: TeamEventRecordSub


class TeamEventResponse(BaseModel):
    team_number: int
    event_key: str
    year: int
    epa: TeamEpaResponse
    record: TeamEventRecord


# TeamYear schemas
class TeamYearRanks(BaseModel):
    total: Optional[int] = None
    country: Optional[int] = None
    state: Optional[int] = None
    district: Optional[int] = None


class TeamYearResponse(BaseModel):
    team_number: int
    year: int
    epa: TeamEpaResponse
    record: TeamEventRecord
    ranks: TeamYearRanks
    competing: bool = False


# Year schemas
class YearTeamEntry(BaseModel):
    team_number: int
    name: str
    nickname: Optional[str] = None
    city: Optional[str] = None
    state_prov: Optional[str] = None
    country: Optional[str] = None
    rookie_year: Optional[int] = None


class YearEventEntry(BaseModel):
    event_key: str
    name: str
    short_name: Optional[str] = None
    city: Optional[str] = None
    state_prov: Optional[str] = None
    country: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


class YearResponse(BaseModel):
    year: int
    teams: List[YearTeamEntry]
    events: List[YearEventEntry]
