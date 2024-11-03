# Terraform and Terraform-CDK for Azure


This repository contains infrastructure as code (IaC) for deploying resources on Azure using both Terraform (HCL) and Terraform-CDK (Python). The repository is structured to provide examples and reusable modules for managing Azure resources efficiently.

## Repository Structure

- `terraform/`: Contains traditional Terraform (HCL) scripts.
- `terraform-cdk/`: Contains Terraform-CDK (Python) scripts.

## Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) installed.
- [Python](https://www.python.org/downloads/) installed.
- [Node.js](https://nodejs.org/en/download/) installed.
- Azure CLI installed and authenticated (`az login`).

## Getting Started

### Terraform (HCL)

1. Navigate to the `terraform/` directory:
    ```sh
    cd terraform/
    ```

2. Initialize Terraform:
    ```sh
    terraform init
    ```

3. Plan the Terraform configuration:
    ```sh
    terraform plan
    ```

4. Apply the Terraform configuration:
    ```sh
    terraform apply
    ```

### Terraform-CDK (Python)

1. Navigate to the `terraform-cdk/` directory:
    ```sh
    cd terraform-cdk/
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Initialize the CDK project (if not already done):
    ```sh
    cdktf init
    ```

5. Synthesize the Terraform configuration:
    ```sh
    cdktf synth
    ```

6. Plan the Terraform-CDK configuration:
    ```sh
    cdktf plan
    ```

7. Deploy the stack:
    ```sh
    cdktf deploy
    ```

## Project Details

### Terraform (HCL)

The `terraform/` directory contains traditional Terraform scripts written in HCL. The main components include:

- `main.tf`: The main configuration file.
- `variables.tf`: Defines the input variables.