FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]

# docker build
#  docker build -t rest-apis-flask-python .
# docker run
#  run -p 5005:5000 rest-apis-flask-python