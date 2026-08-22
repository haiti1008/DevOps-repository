FROM alpine:latest

RUN apk add --no-cache chrony

COPY chrony.conf /etc/chrony/chrony.conf

CMD ["chronyd", "-d", "-x"]

