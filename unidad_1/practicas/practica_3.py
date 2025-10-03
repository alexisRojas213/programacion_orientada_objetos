
#practica 3 introduciion al polimorfismo simulando un sistema de cobro con multiples opciones de pago 
class pago_tarjeta:
    def procesar_pago(self,cantidad):
        return f"procesando pago $ {cantidad} con tarjeta bancaria"
    
class deposito:
    def procesar_pago(self,cantidad):
        return f"procesando pago por medio de deposito por ${cantidad}"

class transferencia:
    def procesar_pago(self,cantidad):
        return f"procesando pago por medio de transferencia en ventanilla por mdio de ${cantidad}"
    

class paypal:
    def procesar_pago(self, cantidad):
        return f"procesando pago de $ {cantidad} por medio de paypal"
    
#instancia 
metodo_de_pago= [pago_tarjeta(), deposito(), transferencia(), paypal() ]

for m in metodo_de_pago:
    print(m.procesar_pago(500))


#actividad procesar pago con diferentres cantidades en cada una de las formas de pago. ejemplo: 100 con tarjeta,
#  500 con transferencia 200 con paypal y 400 con deposito
pago1=pago_tarjeta()
pago2=deposito()
pago3=transferencia()
pago4=paypal()
#polimorfismo el mismo metodo con diferentes objetos
print(pago1.procesar_pago(100))
print(pago2.procesar_pago(400))
print(pago3.procesar_pago(500))
print(pago3.procesar_pago(200))