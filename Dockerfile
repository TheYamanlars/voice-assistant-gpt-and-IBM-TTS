# Use Python 3.10 as base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------------------------------------------
# Copy certificates for secure OpenAI API access in lab environment
# REMOVE THIS SECTION WHEN DEPLOYING TO PRODUCTION
# Copy the self-signed root CA certificate
COPY certs/rootCA.crt /usr/local/share/ca-certificates/rootCA.crt

# Update CA trust store
RUN chmod 644 /usr/local/share/ca-certificates/rootCA.crt && \
    update-ca-certificates

# Set environment variables for SSL and OpenAI
ENV OPENAI_API_KEY=skills-network
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
# -----------------------------------------------------------------

# Expose port 8000
EXPOSE 8000

# Start the Flask server
CMD ["python", "-u", "server.py"]
