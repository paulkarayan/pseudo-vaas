import shutterstock_sdk
from configular import Configular

from app.dependencies import CONFIG_FILE

config = Configular(CONFIG_FILE)
configuration = shutterstock_sdk.Configuration()
configuration.username = config.get('Shutterstock', 'consumer_key')
configuration.password = config.get('Shutterstock', 'consumer_secret')
client = shutterstock_sdk.ApiClient(configuration)

ss_api = shutterstock_sdk.ImagesApi(client)
