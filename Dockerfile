# Due to using a python builder image, skipping taking the python source image here
# FROM python:3.9-slim

# Establish working folder and copy dependencies
WORKDIR /app
COPY requirements.txt .
RUN python -m venv venv && \
    . /app/venv/bin/activate && \
    pip install -U pip wheel && \
    pip install --no-cache-dir -r requirements.txt
ENV PATH /app/venv/bin:$PATH
# Copy the application contents
COPY service/ ./service/
# Expose the port is expecting in the environment
EXPOSE 8501
# Run the app
CMD ["streamlit", "run", "service/app.py"]