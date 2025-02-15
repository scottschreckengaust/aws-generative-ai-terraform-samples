#syntax=docker/dockerfile:1.4
FROM public.ecr.aws/docker/library/python@sha256:220d07595f288567bbf07883576f6591dad77d824dce74f0c73850e129fa1f46

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y install procps && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Set most of the environment variables from Terraform backend deployment outputs
ENV COGNITO_DOMAIN='<COGNITO_DOMAIN>'
ENV REGION='us-east-1'
ENV USER_POOL_ID='<USER_POOL_ID>'
ENV CLIENT_ID='<CLIENT_ID>'
# CLIENT_SECRET look in AWS Console
ENV CLIENT_SECRET='<CLIENT_SECRET>'
ENV IDENTITY_POOL_ID='<IDENTITY_POOL_ID>'
ENV AUTHENTICATED_ROLE_ARN='<AUTHENTICATED_ROLE_ARN>'
ENV GRAPHQL_ENDPOINT='<GRAPHQL_ENDPOINT>'
ENV S3_INPUT_BUCKET='<S3_INPUT_BUCKET>'
ENV S3_PROCESSED_BUCKET='<S3_PROCESSED_BUCKET>'
ENV CLIENT_NAME='<CLIENT_NAME>'

# Replace APP_URI with the Amazon CloudFront output from Terraform frontend, then deploy Terraform frontend again
ENV APP_URI='http://localhost:8501'
EXPOSE 8501
COPY . .
RUN chmod a+x /app/healthcheck.sh

USER nobody
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "/app/healthcheck.sh" ]
ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=8501"]
