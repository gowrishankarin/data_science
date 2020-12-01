FROM continuumio/miniconda3

WORKDIR /usr/src/app
COPY flask-mini_ubuntu.yml .
RUN conda env create  -f flask-mini_ubuntu.yml
SHELL ["conda", "run", "-n", "flask-mini", "/bin/bash", "-c"]

COPY . .
# CMD ["python", "app.py"]

CMD ["conda", "run", "-n", "flask-mini", "python", "run.py", "-h", "0.0.0.0", "-p", "5000"]

# https://pythonspeed.com/articles/activate-conda-dockerfile/
