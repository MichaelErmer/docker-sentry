FROM dockerrepo.oss.rocks/python:2.7.10

MAINTAINER Hans Kristian Flaatten <hans.kristian.flaatten@turistforeningen.no>
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y libxslt1-dev libxml2-dev \
                       libpq-dev expect libldap2-dev libsasl2-dev libssl-dev \
                       libffi-dev libyaml-dev 

RUN pip install -U virtualenv
RUN virtualenv /www/sentry/
RUN source /www/sentry/bin/activate
RUN pip install -U sentry==8.0.0rc1 sentry-slack
ADD sentry.conf.py /root/.sentry/sentry.conf.py
EXPOSE 8080

#ADD sentry.conf.py /root/.sentry/sentry.conf.py

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /wheels/*

