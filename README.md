# Serviço 2 — Google Cloud Run Functions

Função serverless hospedada no **Google Cloud Platform**, desenvolvida em Python 3.14.

## O que faz

Simula o papel de uma instituição financeira (Banco Beta) no ecossistema Open Finance,
expondo dados do índice de inflação IPCA via endpoint HTTP público.

## Como implantar

1. Acesse o [Google Cloud Console](https://console.cloud.google.com) e faça login
2. Crie um projeto chamado `multicloud-experimento` (se ainda não existir)
3. Busque por **Cloud Run** no menu de navegação
4. Clique em **Escrever uma função > Python**
5. Preencha:
   - **Nome do serviço:** `dados-inflacao`
   - **Região:** `us-central1`
   - **Autenticação:** Permitir acesso público
6. No editor de código:
   - Substitua o conteúdo de `main.py` pelo código deste repositório
   - Substitua o conteúdo de `requirements.txt` pelo arquivo deste repositório
   - **Ponto de entrada da função:** `dados_inflacao`
7. Clique em **Salvar e reimplantar** e aguarde de 1 a 2 minutos
8. Copie a URL gerada

## Resposta esperada

```json
{
  "provedor": "Google Cloud Platform",
  "servico": "Cloud Run Functions",
  "dados_simulados": {
    "instituicao": "Banco Beta (simulado)",
    "produto": "Índice de inflação IPCA",
    "valor": 4.62
  },
  "status": "sucesso"
}
```

## Referência

- [Cloud Run Functions Documentation](https://cloud.google.com/run/docs)
