# paypal_api.py
def simular_resposta_api_paypal_processar_pagamento():
    resposta = {
        "status": "sucesso",
        "mensagem": "Pagamento processado com sucesso",
        "transacao_id": "ABC123XYZ",
        "valor": 100.00,
        "moeda": "USD"
    }
    return resposta

def simular_resposta_api_paypal_processar_reembolso(transacao_id):
    resposta = {
        "status": "sucesso",
        "mensagem": "Reembolso processado com sucesso",
        "transacao_id": transacao_id,
        "valor": 50.00,
        "moeda": "USD"
    }
    return resposta

def simular_resposta_api_paypal_verificar_transacao(transacao_id):
    resposta = {
        "status": "sucesso",
        "mensagem": "Transação encontrada",
        "transacao_id": transacao_id,
        "valor": 100.00,
        "moeda": "USD",
        "data": "2024-04-25 15:30:00",
        "detalhes": "Compra de um produto"
    }
    return resposta


