FROM alpine:3.12.1

RUN apk update
RUN apk add python3
RUN mkdir /web && mkdir /web/files
COPY rpm-server.py /web/rpm-server.py

CMD ["/usr/bin/python3", "/web/rpm-server.py"]
