FROM continuumio/miniconda3

WORKDIR /usr/src/app
COPY environment.yml .
RUN conda env create  -f environment.yml
SHELL ["conda", "run", "-n", "flask-mini", "/bin/bash", "-c"]

COPY . .
# CMD ["python", "app.py"]

CMD ["conda", "run", "-n", "flask-mini", "python", "app.py", "-h", "0.0.0.0", "-p", "5000"]

# https://pythonspeed.com/articles/activate-conda-dockerfile/
