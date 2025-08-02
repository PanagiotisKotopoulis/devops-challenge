#!/bin/bash

# Ensure you're logged in and using the correct subscription
# az login
# az account set --subscription <your-subscription-id>

APP_NAME="backend-app"
RESOURCE_GROUP="devops-rg"

echo "Fetching revisions for $APP_NAME..."
az containerapp revision list \
  --name $APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --query "[].{Name:name, Created:createdTime}" \
  --output table

echo ""
echo "⚠️  Manually copy the name of the revision you want to roll back to."
read -p "Enter revision name to activate: " REVISION

echo "Rolling back to $REVISION ..."
az containerapp revision activate \
  --name $APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --revision $REVISION
