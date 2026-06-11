import json


def lambda_handler(event, context):
    """
    Serviço 1 — Amazon Web Services (AWS Lambda)
    Simula uma instituição financeira expondo dados de câmbio via API REST.
    Parte do ambiente experimental multicloud — Python Computing Club (Faculdade Impacta, 2026).
    """

    dados = {
        "provedor": "Amazon Web Services",
        "servico": "AWS Lambda",
        "regiao": "us-east-1",
        "dados_simulados": {
            "instituicao": "Banco Alpha (simulado)",
            "produto": "Taxa de câmbio USD/BRL",
            "valor": 5.87,
            "unidade": "BRL por USD",
            "contexto": "Simulação Open Finance - Multicloud"
        },
        "status": "sucesso"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(dados, ensure_ascii=False)
    }
