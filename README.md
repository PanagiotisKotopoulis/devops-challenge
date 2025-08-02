# DevOps Challenge Submission

## ✅ Architecture Diagram

```mermaid
graph TD
    subgraph Frontend
        FE[Frontend App (React/HTML)]
    end

    subgraph Backend
        BE[FastAPI Container]
    end

    subgraph Observability
        AI[Application Insights]
        LA[Log Analytics Workspace]
    end

    subgraph Azure Infra
        ACA[Azure Container Apps]
        TF[Terraform]
    end

    FE -->|HTTP Request| ACA
    ACA -->|Routes to| BE
    BE -->|Env Logs| AI
    AI --> LA
```

---

## 🛠 Tech Stack & Tooling

| Layer | Tooling |
|-------|---------|
| Application | FastAPI, Python |
| Frontend | HTML/CSS (static) |
| Containerization | Docker |
| Infra as Code | Terraform |
| CI/CD | Azure DevOps Pipelines |
| Monitoring | Application Insights, Log Analytics |

---

## 🔄 CI/CD Workflow

1. On push to `master`, pipeline triggers.
2. Pipeline stages:
   - **Build & Test** backend and frontend
   - **Deploy Staging** via Terraform
   - **Manual Approval** before production
   - **Deploy Production** using same Terraform infra
3. **Rollback** supported via CLI or script.

---

## ☁️ Infrastructure Summary (Terraform)

Terraform provisions:
- Azure Resource Group (`devops-rg`)
- Azure Container Apps for frontend & backend
- Azure Log Analytics Workspace
- Azure Application Insights Instance
- Optional Managed Environment

Located in `infra/` directory:
- `main.tf`, `variables.tf`, etc.

---

## 🔐 Security Considerations

- ✅ Environment variables used for secrets (`APPINSIGHTS_INSTRUMENTATIONKEY`)
- ✅ TLS enforced by Azure Ingress
- ✅ No secrets hardcoded in code or repos
- ✅ Azure roles scoped per-resource

---

## ♻️ Rollback & Recovery

Rollback command:
```bash
az containerapp revision list \
  --name backend-app \
  --resource-group devops-rg

az containerapp revision activate \
  --name backend-app \
  --resource-group devops-rg \
  --revision <last-known-good>
```

Scripted version: `rollback.sh`

---

## 📊 Monitoring & Dashboards

- **Azure Monitor** + **Application Insights** connected
- **Logs captured via Log Analytics** workspace

### Dashboards (Workbooks):
1. **Backend - Request Volume**:
```kusto
requests
| summarize count() by bin(timestamp, 5m)
```
Visualization: Time Chart

2. **Backend - Errors**:
```kusto
traces
| where severityLevel >= 3
| summarize count() by bin(timestamp, 5m)
```
Visualization: Time Chart or Table

Both saved and attached to Log Analytics workspace.

---

## ✅ Notes
- DB functionality is mocked.
- App Insights key provided via environment.
- Frontend & backend communicate over HTTPS.
- Monitoring and CI/CD follow minimal, production-ready patterns.

