from app.models.models import DomainSearch
from app.models.models import EmailFinder
from app.models.models import AuthorFinder
from app.models.models import EmailVerifier
from app.models.models import EmailCount
from app.dependencies.hunterio import hunterio_api
from fastapi import APIRouter
from fastapi import HTTPException
import re
import requests
from urllib.parse import urlparse


router = APIRouter(prefix="/email_validation")
domain_rx = re.compile('[a-zA-Z0-9-.]*')
hostname_rx = re.compile('([a-zA-Z0-9-]+.)+[a-zA-z0-9]{2}[a-zA-z0-9]*$')


@router.get('/domain_search')
async def domain_search(domain_search_data: DomainSearch):
    if not domain_search_data.domain and not domain_search_data.company:
        raise HTTPException(
            status_code=400, detail='Either domain or company must be provided')
    print(domain_search_data.domain)
    if domain_search_data.domain and not domain_rx.fullmatch(domain_search_data.domain):
        raise HTTPException(
            status_code=400, detail="Domain must follow the regex '[a-zA-Z0-9-.]*'"
        )
    try:
        params = {k: v for k, v in domain_search_data if v}
        return hunterio_api.domain_search(params)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail='Internal Server Error')


@router.get('/email_finder')
async def email_finder(email_finder_data: EmailFinder):
    if not email_finder_data.domain and not email_finder_data.company:
        raise HTTPException(
            status_code=400, detail='Either domain or company must be provided')
    if email_finder_data.domain and not domain_rx.fullmatch(email_finder_data.domain):
        raise HTTPException(
            status_code=400, detail="Domain must follow the regex '[a-zA-Z0-9\-.]*'"
        )
    if (email_finder_data.first_name or email_finder_data.last_name) and not (email_finder_data.first_name and email_finder_data.last_name):
        raise HTTPException(
            status_code=400, detail='first_name and last_name must be provided together. Otherwise, provide full_name')
    if not email_finder_data.first_name and not email_finder_data.full_name:
        raise HTTPException(status_code=400, detail='Either first_name and last_name must be provided OR full_name')
    try:
        params = {k: v for k, v in email_finder_data if v}
        return hunterio_api.email_finder(params)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail='Internal Server Error')

@router.get('/author_finder')
async def author_finder(author_finder_data: AuthorFinder):
    try:
        url_parsed = urlparse(author_finder_data.url)
        if not hostname_rx.fullmatch(url_parsed.hostname) or url_parsed.scheme not in ('http', 'https'):
            raise HTTPException(status_code=400, detail='Invalid url')
        params = {k: v for k, v in author_finder_data if v}
        res_json = hunterio_api.author_finder(params)
        if res_json.get('errors') is not None:
            raise HTTPException(status_code=400, detail='Invalid url')
        return res_json
    except HTTPException as http_e:
        raise(http_e)
    except Exception as e:
        print('error')
        print(e)
        raise HTTPException(
            status_code=500, detail='Internal Server Error')

@router.get('/email_verifier')
async def email_verifier(email_verifier_data: EmailVerifier):
    try:
        params = {k: v for k, v in email_verifier_data if v}
        return hunterio_api.email_verifier(params)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail='Internal Server Error')


@router.get('/email_count')
async def email_count(email_count_data: EmailCount):
    if not email_count_data.domain and not email_count_data.company:
        raise HTTPException(
            status_code=400, detail='Either domain or company must be provided')
    if email_count_data.domain and not domain_rx.fullmatch(email_count_data.domain):
        raise HTTPException(
            status_code=400, detail="Domain must follow the regex '[a-zA-Z0-9\-.]*'"
        )
    try:
        params = {k: v for k, v in email_count_data if v}
        return hunterio_api.email_count(params)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail='Internal Server Error')