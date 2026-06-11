# Arquitetura do Ambiente Experimental

## Visão Geral

```
┌─────────────────────────────────────────────────────────────────┐
│                    AMBIENTE MULTICLOUD                          │
│                                                                 │
│  ┌──────────────────┐        ┌──────────────────┐              │
│  │   AWS Lambda     │        │  GCP Cloud Run   │              │
│  │  (us-east-1)     │        │  (us-central1)   │              │
│  │                  │        │                  │              │
│  │  Banco Alpha     │        │  Banco Beta      │              │
│  │  Câmbio USD/BRL  │        │  Inflação IPCA   │              │
│  │  Python 3.12     │        │  Python 3.14     │              │
│  └────────┬─────────┘        └────────┬─────────┘              │
│           │   HTTP/REST               │   HTTP/REST             │
│           └──────────────┬────────────┘                        │
│                          │                                     │
│              ┌───────────▼──────────┐                          │
│              │    PythonAnywhere    │                          │
│              │   (Flask Web App)    │                          │
│              │                     │                          │
│              │  Consolidador       │                          │
│              │  Open Finance       │                          │
│              │  Python 3.10        │                          │
│              └─────────────────────┘                          │
│                          │                                     │
│                  GET /consolidar                               │
│                          │                                     │
│              ┌───────────▼──────────┐                          │
│              │  Resposta unificada  │                          │
│              │  JSON com dados      │                          │
│              │  das 3 nuvens        │                          │
│              └─────────────────────┘                          │
└─────────────────────────────────────────────────────────────────┘
```

## Fluxo de dados

1. **AWS Lambda** expõe dados de câmbio via URL pública HTTP
2. **GCP Cloud Run** expõe dados de inflação via URL pública HTTP
3. **PythonAnywhere** agrega os dois e retorna resposta consolidada
4. Toda comunicação usa protocolo **HTTP/REST** com resposta em **JSON**

## Analogia com o Open Finance

| Ambiente experimental     | Open Finance real              |
|---------------------------|-------------------------------|
| AWS Lambda                | Banco A (ex: Itaú)            |
| GCP Cloud Run             | Banco B (ex: Bradesco)        |
| PythonAnywhere            | App agregador (ex: Guiabolso) |
| HTTP/REST + JSON          | APIs padronizadas BCB         |
| Dados simulados           | Dados reais com OAuth 2.0     |

## Protocolo utilizado

- **Transporte:** HTTP/1.1
- **Método:** GET
- **Formato de resposta:** JSON
- **Autenticação:** nenhuma (ambiente acadêmico)
- **Em produção:** OAuth 2.0 + mTLS + TLS 1.3 (conforme BCB, 2023)
