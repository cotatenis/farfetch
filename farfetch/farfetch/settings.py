VERSION = '0-2-0'
BOT_NAME = 'farfetch'
SPIDER_MODULES = ['farfetch.spiders']
NEWSPIDER_MODULE = 'farfetch.spiders'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'

ROBOTSTXT_OBEY = False
# aqui colocamos os valores um pouco abaixo da menor quantidade 
# encontrada ao longo da paginação de cada marca
SPIDERMON_CUSTOM_MIN_ITEMS = {
    'farfetch-male-yeezy' : 60,
    'farfetch-female-yeezy' : 5,
    'farfetch-male-jordan' : 20,
    'farfetch-female-jordan' : 35,
    'farfetch-female-stella' : 25,
    'farfetch-female-adidas' : 60,
    'farfetch-female-nike-x-off-white' : 5,
    "farfetch-female-nike" : 30,
    'farfetch-male-adidas-pw' : 1,
    'farfetch-male-stella' : 1,
    'farfetch-male-adidas' : 70,
    'farfetch-male-nike' : 10,
    'farfetch-male-nike-x-off-white' : 10,
}
MAGIC_FIELDS = {
    "timestamp": "$isotime",
    "spider": "$spider:name",
    "url": "$response:url",
}
SPIDER_MIDDLEWARES = {
    "scrapy_magicfields.MagicFieldsMiddleware": 100,
}
SPIDERMON_ENABLED = True
EXTENSIONS = {
    'farfetch.extensions.SentryLogging' : -1,
    'spidermon.contrib.scrapy.extensions.Spidermon': 500,
}
ITEM_PIPELINES = {
    "farfetch.pipelines.DiscordMessenger" : 100,
    "farfetch.pipelines.FarfetchImagePipeline" : 200,
    "farfetch.pipelines.GCSPipeline": 300,
}
SPIDERMON_SPIDER_CLOSE_MONITORS = (
'farfetch.monitors.SpiderCloseMonitorSuite',
)

SPIDERMON_VALIDATION_DROP_ITEMS_WITH_ERRORS = False
SPIDERMON_PERIODIC_MONITORS = {
'farfetch.monitors.PeriodicMonitorSuite': 30, # time in seconds
}
SPIDERMON_SENTRY_DSN = ""
SPIDERMON_SENTRY_PROJECT_NAME = ""
SPIDERMON_SENTRY_ENVIRONMENT_TYPE = ""
#THROTTLE
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 2
AUTOTHROTTLE_MAX_DELAY = 5

#GCP
GCS_PROJECT_ID = ""
GCP_CREDENTIALS = ""
GCP_STORAGE = ""
GCP_STORAGE_CRAWLER_STATS = ""
#FOR IMAGE UPLOAD
IMAGES_STORE = f''

#DISCORD
DISCORD_WEBHOOK_URL = ""
DISCORD_THUMBNAIL_URL = ""
SPIDERMON_DISCORD_WEBHOOK_URL = ""

#LOG LEVEL
LOG_LEVEL='INFO'