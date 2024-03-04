FROM python:3.11

WORKDIR /code
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .

ENV DISABLE_CONTRACTS=1

RUN python setup.py develop --no-deps

# run it once to see everything OK
CMD ["make test"]
