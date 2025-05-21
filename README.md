Crypto Price Ingestion Pipeline

This project implements a cloud-based data ingestion pipeline that pulls cryptocurrency prices (Bitcoin, Ethereum, Litecoin, and XRP) from the CoinGecko API every hour, stores the data in an Amazon S3 bucket, and provisions infrastructure using Terraform. The pipeline uses AWS Lambda triggered by EventBridge for scheduling and GitHub Actions for continuous deployment.

---

Features

- Fetches live price data for BTC, ETH, LTC, and XRP in USD
- Runs automatically every hour using AWS Lambda and EventBridge
- Saves data as timestamped JSON files in an Amazon S3 bucket
- Infrastructure provisioning with Terraform
- Automated CI/CD with GitHub Actions

---

Architecture Overview

CoinGecko API --> AWS Lambda (hourly trigger by EventBridge) --> Saves JSON data to S3 bucket
Terraform provisions Lambda, EventBridge, and S3 bucket
GitHub Actions automates deployment of Terraform and Lambda code

---

Getting Started

Prerequisites

- AWS account with permissions to create Lambda, S3, EventBridge resources
- Terraform installed locally (v1.0+ recommended)
- AWS CLI configured with credentials
- GitHub repository with your project code

Setup

1. Clone the repo

    git clone https://github.com/emaseku/E-Crypto-Prices.git
    cd crypto-pipeline

2. Configure Terraform variables

    Create a terraform.tfvars file and set:

    db_username = "your_db_username"          (Optional for future DB use)
    db_password = "your_db_password"          (Optional for future DB use)
    region      = "us-east-1"                  Your AWS region

3. Initialize and apply Terraform

    terraform init
    terraform apply

    This will provision the AWS resources: Lambda function, S3 bucket, and EventBridge rule.

4. Deploy Lambda function

Your GitHub Actions workflow automates this on each push to main branch.

---

Usage

- Lambda runs hourly, fetching the latest crypto prices and saving them to S3.
- S3 bucket stores JSON files organized by timestamp under the crypto-prices/ prefix.

---

Project Structure

- handle.py : Lambda handler script that fetches prices and saves to S3
- main.tf : Terraform configuration provisioning all AWS resources
- .github/workflows/main.yml : GitHub Actions workflow for CI/CD

---

Future Enhancements

- Store data in a relational or NoSQL database for advanced querying
- Add alerts for significant price changes
- Build a dashboard for price visualization
- Expand to more cryptocurrencies or stock market data
- Add error handling and retries in Lambda

---

License

MIT License

---

Project link: https://github.com/yourusername/crypto-pipeline
