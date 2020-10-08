FROM registry.access.redhat.com/ubi7/python-38

USER root

RUN mkdir -p /home/app
WORKDIR /home/app
RUN yum -y install https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-7-12.noarch.rpm
RUN yum -y install http://mirror.centos.org/centos/7/os/x86_64/Packages/libXv-1.0.11-1.el7.x86_64.rpm
RUN yum -y install http://mirror.centos.org/centos/7/os/x86_64/Packages/libv4l-0.9.5-4.el7.x86_64.rpm
RUN yum -y install zbar
RUN pip install --upgrade pip
RUN pip install fastapi
RUN pip install pyzbar
RUN pip install --no-cache-dir uvicorn gunicorn
RUN pip install python-multipart
RUN pip install numpy
RUN pip install opencv-python-headless
RUN pip install pillow
RUN pip install celery[redis]


COPY *.py /home/app/
COPY entrypoint.sh /home/app/
RUN chmod +x /home/app/entrypoint.sh

# CMD ["/home/app/entrypoint.sh"]
# ENTRYPOINT ["/opt/app-root/bin/uvicorn main:app --host 0.0.0.0 --port 8000"]
CMD ["celery", "-A", "tasks", "worker", "-l", "INFO", "&"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
