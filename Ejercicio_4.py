def invoice(amount, vat=19):
    """Función de aplica el IVA a una factura.
    Parametros
    amount: Es la cantidad sin IVA
    vat: Es el porcentaje de IVA
    Devuelve el total de la factura una vez aplicado el IVA. 
    """
    return amount + amount*vat/100

print(invoice(1000,10))
print(invoice(1000))