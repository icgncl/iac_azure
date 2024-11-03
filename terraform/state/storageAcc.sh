#! /bin/bash
ENV=$1

# NOTE : az login if needed
# az login

az group create \
    --name "${ENV}-rg" \
    --location "westeurope"

# Create a storage account for the Terraform state
az storage account create \
    --name "tfstateicg${ENV}" \
    --resource-group "${ENV}-rg" \
    --location "westeurope" \
    --sku "Standard_LRS"

az storage container create \
    --name "tfstateicg${ENV}" \
    --account-name "tfstateicg${ENV}"

