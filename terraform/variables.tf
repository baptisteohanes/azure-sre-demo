variable "prefix" {
  description = "Naming prefix for all resources"
  type        = string
  default     = "memdemo"
}

variable "location" {
  description = "Azure region for all resources"
  type        = string
  default     = "westeurope"
}

variable "subscription_id" {
  description = "Azure subscription ID (required for azurerm v4.x). Can also be set via ARM_SUBSCRIPTION_ID env var."
  type        = string
  default     = null
}

variable "resource_group_name" {
  description = "Name of the existing resource group to deploy into"
  type        = string
}

variable "image_name" {
  description = "Docker image repository name in ACR"
  type        = string
  default     = "memory-demo"
}

variable "image_tag" {
  description = "Docker image tag"
  type        = string
  default     = "latest"
}
