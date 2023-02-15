FROM python:3

ADD app/db.py /
ADD app/main.py /
ADD app/models.py /
ADD app/data_generator.py /

RUN pip install sqlalchemy
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install joblib
COPY . .

EXPOSE 8000
WORKDIR "/app"
CMD [ "/bin/bash", "-c", "/usr/local/bin/python data_generator.py && /usr/local/bin/python db.py && /usr/local/bin/uvicorn main:app --host 0.0.0.0 --port 8000" ]

#CMD ["/usr/local/bin/python data_generator.py && /usr/local/bin/python db.py && /usr/local/bin/uvicorn main:app --host 0.0.0.0 --port 8000"]
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
