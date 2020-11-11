FROM python:slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./nanyang_virus_inline_bot ./nanyang_virus_inline_bot
CMD ["python", "-m", "nanyang_virus_inline_bot.__main__"]
