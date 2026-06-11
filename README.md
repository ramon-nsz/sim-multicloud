# Ambiente Experimental Multicloud — Simulação de Operação Financeira

**Disciplina:** Integração e Desenvolvimento de Sistemas  
**Curso:** Sistemas de Informação — Faculdade Impacta  
**Grupo:** Python Computing Club  
**Ano:** 2026

---

## Sobre o projeto

Este repositório contém o código do ambiente experimental multicloud desenvolvido como parte do artigo acadêmico **"Multicloud: Integração de Sistemas, Desenvolvimento e Aplicações Práticas"**.

O experimento demonstra, em escala reduzida, a arquitetura de integração utilizada na **Simulação de Operação Financeira** no contexto de multicloud: três provedores de nuvem distintos se comunicando via APIs REST padronizadas, sem dependência de infraestrutura compartilhada.

---

## Arquitetura

```
AWS Lambda          GCP Cloud Run        PythonAnywhere
(Banco Alpha)  ──►  (Banco Beta)   ──►   (Consolidador)
Câmbio USD/BRL      Inflação IPCA         Resposta unificada
Python 3.12         Python 3.14           Python 3.10 / Flask
```

Cada serviço simula uma instituição financeira independente expondo dados via API REST,
exatamente como ocorre no ecossistema Open Finance regulado pelo Banco Central do Brasil.

---

## Estrutura do repositório

```
multicloud-openfinance/
│
├── aws-lambda/
│   ├── lambda_function.py   # Código da função Lambda (dados de câmbio)
│   └── README.md            # Instruções de deploy na AWS
│
├── gcp-cloudrun/
│   ├── main.py              # Código da Cloud Run Function (dados de inflação)
│   ├── requirements.txt     # Dependências Python
│   └── README.md            # Instruções de deploy no GCP
│
├── pythonanywhere/
│   ├── flask_app.py         # Aplicação Flask consolidadora
│   └── README.md            # Instruções de deploy no PythonAnywhere
│
├── docs/
│   └── arquitetura.md       # Diagrama e explicação da arquitetura
│
└── README.md                # Este arquivo
```

---

## Endpoints ativos

| Provedor        | Serviço           | Dado simulado         |
|-----------------|-------------------|-----------------------|
| AWS Lambda      | dados-open-finance | Taxa de câmbio USD/BRL |
| GCP Cloud Run   | dados-inflacao    | Inflação IPCA          |
| PythonAnywhere  | /consolidar       | Resposta integrada     |

---

## Como reproduzir o ambiente

### Pré-requisitos

- Conta gratuita na [AWS](https://aws.amazon.com/free/) (cartão necessário para verificação, sem cobrança)
- Conta gratuita no [Google Cloud](https://cloud.google.com/free) ($300 de crédito por 90 dias)
- Conta gratuita no [PythonAnywhere](https://www.pythonanywhere.com) (sem cartão)

### Passo a passo

**1. Deploy do AWS Lambda**

Siga as instruções em [`aws-lambda/README.md`](aws-lambda/README.md).
Guarde a URL gerada no formato:
```
https://XXXXXXXX.lambda-url.us-east-1.on.aws/
```

**2. Deploy do GCP Cloud Run**

Siga as instruções em [`gcp-cloudrun/README.md`](gcp-cloudrun/README.md).
Guarde a URL gerada no formato:
```
https://dados-inflacao-XXXXXXX.us-central1.run.app
```

**3. Deploy do PythonAnywhere**

Siga as instruções em [`pythonanywhere/README.md`](pythonanywhere/README.md).

**4. Testando a integração**

Acesse no navegador:
```
https://SEU_USUARIO.pythonanywhere.com/consolidar
```

A resposta esperada é:
```json
{
  "provedor_consolidador": "PythonAnywhere",
  "descricao": "Consolidação multicloud - Simulação Open Finance",
  "dados_integrados": {
    "fonte_aws": {
      "instituicao": "Banco Alpha (simulado)",
      "produto": "Taxa de câmbio USD/BRL",
      "valor": 5.87
    },
    "fonte_gcp": {
      "instituicao": "Banco Beta (simulado)",
      "produto": "Índice de inflação IPCA",
      "valor": 4.62
    }
  },
  "status": "sucesso - três provedores integrados"
}
```

---

## Tecnologias utilizadas

| Tecnologia         | Versão   | Uso                              |
|--------------------|----------|----------------------------------|
| Python             | 3.10–3.14| Linguagem principal              |
| Flask              | 3.x      | Framework web (PythonAnywhere)   |
| AWS Lambda         | —        | Função serverless (AWS)          |
| Cloud Run Functions| —        | Função serverless (GCP)          |
| HTTP/REST + JSON   | —        | Protocolo de comunicação         |
| Functions Framework| 3.x      | Wrapper HTTP para GCP            |

---

## Limitações do ambiente acadêmico

1. Dados simulados — não provenientes de fontes financeiras reais
2. Sem autenticação OAuth 2.0 entre os serviços (simplificado para fins acadêmicos)
3. PythonAnywhere (plano gratuito) não permite chamadas HTTP para `.on.aws`
4. Sem alta disponibilidade ou tolerância a falhas

Em produção, o ambiente exigiria OAuth 2.0 + mTLS + TLS 1.3, conforme exigido pelo
Banco Central do Brasil para o ecossistema Open Finance.

---

## Referências

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Google Cloud Run Documentation](https://cloud.google.com/run/docs)
- [PythonAnywhere Help](https://help.pythonanywhere.com)
- [Open Finance Brasil — BCB](https://www.bcb.gov.br/estabilidadefinanceira/openfinance)
- [Flask Documentation](https://flask.palletsprojects.com)
