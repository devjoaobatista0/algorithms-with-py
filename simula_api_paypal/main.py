import metodo_pag


class Ecomerce:
    def __init__(self) -> None:
        pass
    
    def pagamento(self, metodo):
        return metodo_pag.chamar_metodo(metodo)
        
        
        
ecomerce = Ecomerce()
resposta = ecomerce.pagamento('processar_pagamento')
pagou = input('Cliente pagou ?')

if pagou == 'sim':
    print (resposta)
    
else:
    print('pagamento nao processado')

        

        
    

