# metodo_pag.py
import api_paypal as paypal

def processar_pagamento():
    return paypal.simular_resposta_api_paypal_processar_pagamento()

def processar_reembolso(transacao_id):
    return paypal.simular_resposta_api_paypal_processar_reembolso(transacao_id)

def verificar_transacao(transacao_id):
    return paypal.simular_resposta_api_paypal_verificar_transacao(transacao_id)

def chamar_metodo(metodo, *args):
    if metodo == "processar_pagamento":
        return processar_pagamento()
    elif metodo == "processar_reembolso":
        return processar_reembolso(*args)
    elif metodo == "verificar_transacao":
        return verificar_transacao(*args)
    else:
        return {"status": "erro", "mensagem": "Método não encontrado"}





