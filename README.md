░█████╗░░█████╗░████████╗░█████╗░████████╗███████╗███╗░░██╗██╗░██████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝████╗░██║██║██╔════╝
██║░░╚═╝██║░░██║░░░██║░░░███████║░░░██║░░░█████╗░░██╔██╗██║██║╚█████╗░
██║░░██╗██║░░██║░░░██║░░░██╔══██║░░░██║░░░██╔══╝░░██║╚████║██║░╚═══██╗
╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║░░░██║░░░███████╗██║░╚███║██║██████╔╝
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░


--------------------------------------------------------------------------

# Web crawler

url: [https://www.farfetch.com/br/](https://www.farfetch.com/br/)

# 1. Configuration
Before you run this project and for the proper running of this program you need to set up some variables inside `farfetch/farfetch/settings.py`.

## 1.1 SENTRY
This project utilizes [SENTRY](https://sentry.io/) for error tracking.

- `SPIDERMON_SENTRY_DSN`
- `SPIDERMON_SENTRY_PROJECT_NAME`
- `SPIDERMON_SENTRY_ENVIRONMENT_TYPE`

## 1.2 GOOGLE CLOUD PLATFORM

- `GCS_PROJECT_ID` 
- `GCP_CREDENTIALS`
- `GCP_STORAGE`
- `GCP_STORAGE_CRAWLER_STATS`
- `IMAGES_STORE`

## 1.3 DISCORD
- `DISCORD_WEBHOOK_URL`
- `DISCORD_THUMBNAIL_URL`
- `SPIDERMON_DISCORD_WEBHOOK_URL`


# 2. Implemented Brands
- `farfetch-male-yeezy` [`YeezyMaleSpider`]
- `farfetch-female-yeezy` [`YeezyFemaleSpider`]
- `farfetch-male-jordan` [`JordanMaleSpider`]
- `farfetch-female-jordan` [`farfetch-female-jordan`]
- `farfetch-female-stella` [`AdidasStellaFemaleSpider`]
- `farfetch-female-adidas` [`AdidasFemaleSpider`]
- `farfetch-female-nike-x-off-white` [`NikeXOffWhiteFemaleSpider`]
- `farfetch-female-nike` [`NikeFemaleSpider`]
- `farfetch-male-adidas-pw` [`AdidasPWMaleSpider`]
- `farfetch-male-stella` [`AdidasStellaMaleSpider`]
- `farfetch-male-adidas` [`AdidasMaleSpider`]
- `farfetch-male-nike` [`NikeMaleSpider`]
- `farfetch-male-nike-x-off-white` [`NikeXOffWhiteMaleSpider`]

# 3. Build

```shell
cd farfetch
make docker-build-production
```

# 4. Publish

```shell
make docker-publish-production
```

# 5. Use
- The parameter `brand` could receive one of the following values:[`farfetch-male-yeezy`, `farfetch-female-yeezy`,  `farfetch-male-jordan`, `farfetch-female-jordan`, `farfetch-female-stella`, `farfetch-female-adidas`,
 `farfetch-female-nike-x-off-white`, `farfetch-female-nike`, `farfetch-male-adidas-pw`, `farfetch-male-stella`, `farfetch-male-adidas`, `farfetch-male-nike`, `farfetch-male-nike-x-off-white`].
- The parameter `page-number` must receive an integer.

```shell
docker run --shm-size="2g" gcr.io/cotatenis/cotatenis-crawl-farfetch:0.2.0 --brand=farfetch-male-stella --page-number=1
```