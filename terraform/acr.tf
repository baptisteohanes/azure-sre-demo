resource "azurerm_container_registry" "main" {
  name                = "acr${replace(var.prefix, "-", "")}"
  resource_group_name = data.azurerm_resource_group.main.name
  location            = data.azurerm_resource_group.main.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "null_resource" "docker_build" {
  triggers = {
    dockerfile_hash   = filemd5("${path.module}/../Dockerfile")
    app_hash          = filemd5("${path.module}/../app.py")
    requirements_hash = filemd5("${path.module}/../requirements.txt")
  }

  provisioner "local-exec" {
    command = "az acr build --registry ${azurerm_container_registry.main.name} --image ${var.image_name}:${var.image_tag} --file ${path.module}/../Dockerfile ${path.module}/../"
  }

  depends_on = [azurerm_container_registry.main]
}
