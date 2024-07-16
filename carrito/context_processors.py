def total_carrito_transferencia(request):
    total = 0
    if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado_transferencia"])
    return {"total_carrito_transferencia": total}

def total_carrito_normal(request):
    total = 0
    if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado_normal"])
    return {"total_carrito_normal": total}