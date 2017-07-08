FROM google/python

RUN pip install --upgrade pip
RUN pip install --upgrade google-api-python-client
RUN pip install redis

ADD producer.py /producer.py
ADD consumer.py /consumer.py
ADD node.py /node.py

CMD python node.py