FROM ubuntu
RUN apt update && apt -y install python3
COPY main.py /opt
ENTRYPOINT ["python3"]
CMD ["opt/main.py"]