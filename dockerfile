# Use the official Alpine Linux image as the base image
FROM alpine:latest

WORKDIR /app

RUN echo "echo 'Hello, world!'" > hello.sh
