FROM tiangolo/uwsgi-nginx-flask:python3.7

# Optionally, install some typical packages used for building and network debugging.
RUN apt-get update

# Update to the latest PIP
RUN pip3 install --upgrade pip

WORKDIR /app

# Copy our files into the current working directory WORKDIR
COPY ./ ./

# install our dependencies
RUN  pip3 install -r requirements.txt

CMD ["python3", "-m", "main"]

EXPOSE 80