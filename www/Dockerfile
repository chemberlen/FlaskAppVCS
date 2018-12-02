FROM ubuntu:16.04

RUN groupadd -r teofedryn --gid=1000 && useradd -r -g teofedryn --uid=1000 teofedryn

RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-venv && apt-get install python-pip -y

WORKDIR home/teofedryn/www

COPY . ./

RUN python3 -m venv venv

ENV FLASK_APP start/start.py
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

RUN venv/bin/pip install -r requirements.txt

RUN chown -R teofedryn:teofedryn ./

USER teofedryn

CMD ["/bin/bash"]



#CMD ["/home/teofedryn/www/venv/bin/activate"]

#RUN python -m venv venv
#RUN venv/bin/pip install -r requirements.txt
#RUN venv/bin/pip install gunicorn
#
#RUN chmod +x boot.sh
#
#ENV FLASK_APP start/start.py
#
#RUN chown -R www:www ./
#USER www
#
#EXPOSE 5000
#ENTRYPOINT ["./boot.sh"]
