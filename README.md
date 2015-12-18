# Sentry on Docker Compose

This is a production ready setup of
[Sentry](https://github.com/getsentry/sentry) with Postgres and Redis using
[Docker Compose](https://github.com/docker/fig).

![Docker Compose container overview](https://docs.google.com/drawings/d/1OB0R9QUec7hytx73EYHJcmLzj2m6bMNWnNv-nePAg24/pub?w=766&h=216)

## What are the requirements?

* [Docker](https://github.com/docker/docker) >= `v1.3`
* [Docker Compose](https://github.com/docker/fig) >= `v1.1.0-rc2`

## How do I start this thing?

```
docker-compose up
```

## How do I install/update this thing?

Run this once to do the DB migrations and create a first superuser.

```
docker-compose run www upgrade
```

## How do I find the exposed port?

```
docker-compose port www 8080
```

## How do I add a user?

```
docker-compose run www createuser
```

## How do I configure stuff?

The `sentry.conf.py` holds all the Sentry configurations. Your secret stuff,
however, has to be put into your env.

## Example ENV secret/environment.sh
```
SECRET_KEY=please generate this
SERVER_EMAIL=sentry@foo.bar
SENTRY_URL_PREFIX=https://sentry.foo.bar
```

optional:
```
EMAIL_HOST=mail.foo.bar
EMAIL_PORT=25
EMAIL_HOST_USER=mailer
EMAIL_HOST_PASSWORD=qwert123
EMAIL_USE_TLS=False
ALLOW_REGISTRATION=True # defaults to False, remove to set to False as
ALLOW_SSO=True # defaults to False
```

## [MIT Licensed](https://github.com/Turistforeningen/sentry/blob/master/LICENSE)

