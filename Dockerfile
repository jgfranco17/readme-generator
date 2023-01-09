# Use alpine version 
FROM python3.10-alpine

# Download Package Information
RUN apt-get update -y

# Install Tkinter
RUN apt-get install tk -y

COPY ./main /main

# Run Tkinter
ENTRYPOINT ["python3", "app.py"]