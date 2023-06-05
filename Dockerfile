# syntax=docker/dockerfile:1
FROM python:3.9.16

WORKDIR /usr/src/app

RUN apt-get -y update && apt-get install -y ffmpeg awscli
# Update pip
RUN pip install --upgrade pip
RUN pip install virtualenv
RUN virtualenv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Use virtualenv
RUN /opt/venv/bin/pip install flask requests torch torchvision backgroundremover flask-caching pillow

COPY . .

EXPOSE 80

CMD ["python", "./bgremove.py"]
