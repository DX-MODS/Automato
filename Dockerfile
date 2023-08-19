FROM python:3.10
WORKDIR /app
COPY . /app/
RUN apt update && apt upgrade -y && apt install ffmpeg python3 python3-pip -y
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]
