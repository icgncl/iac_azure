variable "location" {
  description = "The Azure region where resources will be created"
  type        = string
  default     = "westeurope"
}

variable "environment" {
  description = "The environment name"
  type        = string
  default     = "dev"
}

variable "vnet_address_space" {
  description = "The address space for the virtual network"
  type        = list(string)
  default     = ["10.0.0.0/16"]
}

variable "frontend_subnet_address_prefixes" {
    description = "The address prefixes for the frontend subnet"
    type        = list(string)
    default     = ["10.0.1.0/24"]
}

variable "backend_subnet_address_prefixes" {
    description = "The address prefixes for the backend subnet"
    type        = list(string)
    default     = ["10.0.2.0/24"]
}