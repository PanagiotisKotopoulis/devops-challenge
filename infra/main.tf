provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "devops-challenge-rg"
  location = var.location
}

resource "azurerm_container_app_environment" "env" {
  name                = "devops-container-env"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_container_app" "backend" {
  name                         = "quote-api-backend"
  container_app_environment_id = azurerm_container_app_environment.env.id
  resource_group_name          = azurerm_resource_group.rg.name
  revision_mode                = "Single"

  template {
    container {
      name   = "quote-api"
      image  = "nginx"  # Replace later with your own Docker image
      cpu    = 0.5
      memory = "1.0Gi"
    }
  }

  ingress {
    external_enabled = true
    target_port      = 80
    transport        = "auto"

    traffic_weight {
    percentage      = 100
    latest_revision = true
  }
}

