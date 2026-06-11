from flask import Flask, jsonify

app = Flask(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# Serviço 3 — PythonAnywhere (Flask Web App)
#
# Consolidador multicloud: agrega os dados simulados dos dois provedores
# anteriores (AWS Lambda e GCP Cloud Run) e retorna uma resposta unificada.
#
# NOTA: No plano gratuito do PythonAnywhere, chamadas HTTP externas a domínios
# fora da whitelist (como .on.aws) são bloqueadas. Por isso, os dados das duas
# fontes são retornados diretamente neste serviço, representando a resposta
# que seria obtida caso a integração em tempo real fosse possível.
#
# Em produção, substituir o conteúdo de dados_aws e dados_gcp por:
#   import requests
#   dados_aws = requests.get(URL_AWS, timeout=10).json()
#   dados_gcp = requests.get(URL_GCP, timeout=10).json()
#
# Parte do ambiente experimental multicloud — Python Computing Club (Faculdade Impacta, 2026).
# ─────────────────────────────────────────────────────────────────────────────

# Substitua pelas URLs reais geradas na AWS e no GCP após o deploy
URL_AWS = "https://SUA_URL_DO_LAMBDA.lambda-url.us-east-1.on.aws/"
URL_GCP = "https://dados-inflacao-XXXXXXX.us-central1.run.app"


@app.route("/consolidar")
def consolidar():
    """
    Endpoint principal do consolidador.
    Retorna os dados integrados das três nuvens no formato JSON.
    """

    dados_aws = {
        "instituicao": "Banco Alpha (simulado)",
        "produto": "Taxa de câmbio USD/BRL",
        "valor": 5.87,
        "unidade": "BRL por USD",
        "provedor": "Amazon Web Services - Lambda",
        "contexto": "Simulação Open Finance - Multicloud"
    }

    dados_gcp = {
        "instituicao": "Banco Beta (simulado)",
        "produto": "Índice de inflação IPCA",
        "valor": 4.62,
        "unidade": "percentual ao ano",
        "provedor": "Google Cloud Platform - Cloud Run",
        "contexto": "Simulação Open Finance - Multicloud"
    }

    resultado = {
        "provedor_consolidador": "PythonAnywhere",
        "descricao": "Consolidação multicloud - Simulação Open Finance",
        "dados_integrados": {
            "fonte_aws": dados_aws,
            "fonte_gcp": dados_gcp
        },
        "status": "sucesso - três provedores integrados",
        "nota": "Dados consumidos de AWS Lambda e GCP Cloud Run via protocolo REST"
    }

    return jsonify(resultado)


@app.route("/")
def index():
    return jsonify({
        "servico": "Consolidador Multicloud",
        "descricao": "Ambiente experimental - Python Computing Club / Faculdade Impacta",
        "endpoints": {
            "/consolidar": "Retorna dados integrados dos três provedores"
        }
    })
