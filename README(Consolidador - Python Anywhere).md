# Serviço 3 — PythonAnywhere (Consolidador)

Aplicação Flask hospedada no **PythonAnywhere**, desenvolvida em Python 3.10.

## O que faz

Atua como o **agregador multicloud**: simula o papel de um consolidador do Open Finance,
reunindo os dados das duas instituições financeiras (AWS e GCP) em uma única resposta JSON.

## Como implantar

1. Acesse [pythonanywhere.com](https://www.pythonanywhere.com) e crie uma conta gratuita
2. No dashboard, clique em **Web > Add a new web app**
3. Escolha **Flask** e **Python 3.10**, clique em Next até criar
4. No menu **Files**, navegue até `/home/SEU_USUARIO/mysite/`
5. Clique em `flask_app.py`, apague o conteúdo e cole o código deste repositório
6. Salve com **Ctrl+S**
7. Volte à aba **Web** e clique em **Reload**
8. Acesse: `https://SEU_USUARIO.pythonanywhere.com/consolidar`

## Resposta esperada

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

## Observação sobre o plano gratuito

O plano gratuito do PythonAnywhere restringe chamadas HTTP externas a uma whitelist
de domínios. O domínio `.on.aws` (Lambda) não está incluído. Por isso, os dados
são retornados diretamente no código, representando o resultado da integração.
Em produção com plano pago, substituir pelos blocos `requests.get()` comentados no código.

## Referência

- [PythonAnywhere Help](https://help.pythonanywhere.com)
- [Flask Documentation](https://flask.palletsprojects.com)
