FROM registry.access.redhat.com/ubi7/python-38

USER root

RUN mkdir -p /home/app
WORKDIR /home/app

RUN pip install --upgrade pip
RUN pip install fastapi
RUN pip install pyzbar
RUN pip install uvicorn
RUN pip install python-multipart
RUN pip install numpy
RUN pip install opencv-python-headless

COPY *.py /home/app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
