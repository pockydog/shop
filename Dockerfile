FROM python
MAINTAINER vickychen@gillygaming888.com
LABEL version = '1.0'


COPY requirements.txt .
COPY src .


RUN pip --no-cache-dir install -r requirements.txt

ARG PRODUCT_NAME='app'
RUN mkdir -p /${PRODUCT_NAME}
WORKDIR /${PRODUCT_NAME}



