# Configure Azure Provider
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
  backend "azurerm" {}  # Empty block - details will come from backend.hcl
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}
}

# Fetch the resource group
data "azurerm_resource_group" "rg" {
  name     = "${var.environment}-rg"
} 

# Virtual Network
resource "azurerm_virtual_network" "vnet" {
    name = "terraform-vnet"
    resource_group_name = data.azurerm_resource_group.rg.name
    location = var.location
    address_space = var.vnet_address_space

    tags = {
        managed_by = "terraform"
    }
}

# Subnets
resource "azurerm_subnet" "frontend" {
  name                 = "frontend-subnet"
  resource_group_name  = data.azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = var.frontend_subnet_address_prefixes
}

resource "azurerm_subnet" "backend" {
  name                 = "backend-subnet"
  resource_group_name  = data.azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = var.backend_subnet_address_prefixes
}

