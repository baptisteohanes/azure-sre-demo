output "container_app_fqdn" {
  description = "The FQDN of the deployed Container App"
  value       = azurerm_container_app.main.ingress[0].fqdn
}

output "acr_login_server" {
  description = "The login server URL for the Azure Container Registry"
  value       = azurerm_container_registry.main.login_server
}

output "appinsights_connection_string" {
  description = "Application Insights connection string"
  value       = azurerm_application_insights.main.connection_string
  sensitive   = true
}
