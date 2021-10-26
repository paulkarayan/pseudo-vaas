from enum import Enum

from pydantic import BaseModel
from pydantic import validator
from pydantic import validate_email
from pydantic.schema import Optional


class Extractor(str, Enum):
    MONKEY_LEARN = 'monkey_learn'
    SHUTTERSTOCK = 'shutterstock'


class TextSearch(BaseModel):
    text: str
    extractor: Optional[Extractor]

    class Config:
        use_enum_values = True



# For email-validation.py routes
class Department(str, Enum):
    EXECUTIVE = 'executive'
    IT = 'it'
    FINANCE = 'finance'
    MANAGEMENT = 'management'
    SALES = 'sales'
    LEGAL = 'legal'
    SUPPORT = 'support'
    HR = 'hr'
    MARKETING = 'marketing'
    COMMUNICATION = 'communication'

class Seniority(str, Enum):
    JUNIOR = 'junior'
    SENIOR = 'senior'
    EXECUTIVE = 'executive'

class EmailType(str, Enum):
    PERSONAL = 'personal'
    GENERIC = 'generic'

class DomainSearch(BaseModel):
    domain: str = None
    company: str = None
    limit: int = 10
    offset: int = 0
    type: Optional[EmailType]
    seniority: Optional[Seniority]
    department: Optional[Department]    

class EmailFinder(BaseModel):
    domain: str = None
    company: str = None
    first_name: str = None
    last_name: str = None
    full_name: str = None
    max_duration: int = 5

    @validator('full_name', pre=True, always=True, whole=True)
    def check_full_name(cls, full_name):
        if full_name and ' ' not in full_name:
            raise(ValueError('Did not provide a parsable full_name. First and Last name must be separated by a space'))
        return full_name

    @validator('max_duration', pre=True, always=True, whole=True)
    def check_max_duration(cls, max_duration):
        if not 3 <= max_duration <= 20:
            raise(ValueError('max_duration must be between 3 and 20'))
        return max_duration


class AuthorFinder(BaseModel):
    url: str
    max_duration: int = 10

    @validator('max_duration', pre=True, always=True, whole=True)
    def check_max_duration(cls, max_duration):
        if not 3 <= max_duration <= 20:
            raise(ValueError('max_duration must be between 3 and 20'))
        return max_duration

class EmailVerifier(BaseModel):
    email: str

    @validator('email')
    def check_email(cls, email):
        if not validate_email(email):
            raise(ValueError('Invalid Email'))
        return email

class EmailCount(BaseModel):
    domain: str = None
    company: str = None