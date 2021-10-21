from configular import Configular
from monkeylearn import MonkeyLearn

from app.dependencies import CONFIG_FILE

KEYWORD_EXTRACTOR_MODEL_ID = 'ex_YCya9nrn'

config = Configular(CONFIG_FILE)
api_key = config.get('MonkeyLearn', 'api_key')
ml_api = MonkeyLearn(api_key)
