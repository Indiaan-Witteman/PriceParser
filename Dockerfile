# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the entire app into the container at /app
COPY . /app

# Copy the .env file into the container
COPY .env /app/.env

# Check if the .env file exists
RUN test -f .env || (echo ".env file is missing!" && exit 1)

# Check if OPENAI_API_KEY is present in .env
RUN grep -q "OPENAI_API_KEY=" .env || (echo "OPENAI_API_KEY is missing in .env!" && exit 1)

# Set environment variables from the .env file
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    echo "Installing dependencies" && \
    pip install -e .

# Expose the port the app runs on
EXPOSE 8050

# Run the Dash app
CMD ["python", "src/PriceParser/services/demo_service/parser_demo.py"]
