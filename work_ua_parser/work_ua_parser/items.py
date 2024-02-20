import scrapy
from dataclasses import dataclass


@dataclass
class CandidateItem:
    work_ua_id: str
    position: str
    experience: int
    skills: dict
    html: str
    website_link: str
    salary: int
    name: str
