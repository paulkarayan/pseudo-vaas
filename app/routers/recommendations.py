from collections import defaultdict

import shutterstock_sdk
from fastapi import APIRouter

from app.models.models import TextSearch
from ..dependencies.monkey_learn import KEYWORD_EXTRACTOR_MODEL_ID
from ..dependencies.monkey_learn import ml_api
from ..dependencies.shutterstock import ss_api
from ..models.models import Extractor

router = APIRouter(prefix="/recommendations")

LIMIT_PER_KEYWORD = 10


@router.post("/text_to_images")
async def text_to_images(text_search: TextSearch):
    # Search keywords using MonkeyLearn
    if text_search.extractor and text_search.extractor == Extractor.MONKEY_LEARN:
        response = ml_api.extractors.extract(KEYWORD_EXTRACTOR_MODEL_ID, data=[text_search.text]).body
        keywords = [extraction['parsed_value'] for extraction in response[0]['extractions']]
    # Search keywords using Shutterstock
    elif not text_search.extractor or text_search.extractor == Extractor.SHUTTERSTOCK:
        body = shutterstock_sdk.SearchEntitiesRequest(text_search.text)
        keywords = ss_api.get_image_keyword_suggestions(body).keywords
    else:
        return "Invalid extractor value"

    urls = defaultdict(list)
    for keyword in keywords:
        images = ss_api.search_images(query=keyword, per_page=LIMIT_PER_KEYWORD).data
        for image in images:
            urls[keyword].append(f'https://www.shutterstock.com/image-photo/{image.id}')
    return urls
