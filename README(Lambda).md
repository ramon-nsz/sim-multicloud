# Serviço 1 — AWS Lambda

Função serverless hospedada na **Amazon Web Services**, desenvolvida em Python 3.12.

## O que faz

Simula o papel de uma instituição financeira (Banco Alpha) no ecossistema Open Finance,
expondo dados de câmbio USD/BRL via endpoint HTTP público.

## Como implantar

1. Acesse o [console da AWS](https://console.aws.amazon.com) e faça login
2. Busque por **Lambda** e clique em **Criar função**
3. Preencha:
   - **Nome:** `dados-open-finance`
   - **Runtime:** Python 3.12
   - **Arquitetura:** x86_64
4. Na aba **Código**, abra `lambda_function.py`, apague o conteúdo e cole o código deste arquivo
5. Clique em **Deploy**
6. Vá em **Configuração > URL da função > Criar URL da função**
   - Autenticação: `NONE`
   - Clique em **Salvar**
7. Copie a URL gerada — será usada pelo consolidador

## Resposta esperada

```json
{
  "provedor": "Amazon Web Services",
  "servico": "AWS Lambda",
  "regiao": "us-east-1",
  "dados_simulados": {
    "instituicao": "Banco Alpha (simulado)",
    "produto": "Taxa de câmbio USD/BRL",
    "valor": 5.87,
    "unidade": "BRL por USD"
  },
  "status": "sucesso"
}
```

## Referência

- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [AWS Lambda Function URLs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html)
