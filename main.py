import functions_framework
import json


@functions_framework.http
def dados_inflacao(request):
    """
    Serviço 2 — Google Cloud Platform (Cloud Run Functions)
    Simula uma instituição financeira expondo dados de inflação via API REST.
    Parte do ambiente experimental multicloud — Python Computing Club (Faculdade Impacta, 2026).
    """

    dados = {
        "provedor": "Google Cloud Platform",
        "servico": "Cloud Run Functions",
        "regiao": "us-central1",
        "dados_simulados": {
            "instituicao": "Banco Beta (simulado)",
            "produto": "Índice de inflação IPCA",
            "valor": 4.62,
            "unidade": "percentual ao ano",
            "contexto": "Simulação Open Finance - Multicloud"
        },
        "status": "sucesso"
    }

    return json.dumps(dados, ensure_ascii=False), 200, {"Content-Type": "application/json"}
