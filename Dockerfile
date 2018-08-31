FROM ubuntu:latest

RUN apt update && \
 apt install -y python3 python-pip python3-setuptools unzip wget && \
 pip install --upgrade pip==9.0.3 && \
 pip install virtualenv 

RUN virtualenv /opt/web2py && \
 cd /opt/ && \
 rm -f web2py_src.zip && \
 wget -c https://mdipierro.pythonanywhere.com/examples/static/nightly/web2py_src.zip && \
 unzip -o web2py_src.zip && \
 rm -rf /opt/web2py/applications/examples && \
 chmod 755 -R /opt/web2py

ADD private/routes.py /opt/web2py/routes.py

WORKDIR /opt/web2py

EXPOSE 8000

CMD . /opt/web2py/bin/activate && python3 /opt/web2py/web2py.py --nogui --no-banner -a 'pato78IK' -i 0.0.0.0 -p 8000
