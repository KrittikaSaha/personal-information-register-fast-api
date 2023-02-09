FROM python:3

ADD etl/data_generator.py /

RUN pip install sqlalchemy
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install joblib
COPY . .
CMD [ "python", ".etl/data_generator.py" ]

EXPOSE 8000
WORKDIR "/etl"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
