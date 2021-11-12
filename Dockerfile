FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

copy . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "downloader.py" ]

