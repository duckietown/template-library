FROM python:3.7

WORKDIR /duckietown_pondcleaner
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .

RUN find .

ENV DISABLE_CONTRACTS=1

RUN pipdeptree
RUN python setup.py develop --no-deps
# run it once to see everything OK
RUN dt-pc-demo --help
CMD ["dt-pc-demo"]
