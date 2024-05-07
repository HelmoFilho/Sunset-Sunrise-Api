############################################################
# `python-base` sets up all our shared environment variables
############################################################
FROM python:3.11 as python-base

LABEL maintainer="Helmo Filho"

# python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/code"

CMD ["gunicorn",  "src.main:app",  "-k", "uvicorn.workers.UvicornWorker"]

# docker build -t voxus-api .
# docker run -d -p 15000:20000 voxus-api