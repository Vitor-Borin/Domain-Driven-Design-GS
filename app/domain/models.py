def calcular_pegada(data):
    impacto_total = 0

    # Transporte
    transporte = 50 if data['carTravel'] > 100 else 20
    if data['publicTransport'] == "1-3":
        transporte -= 10
    elif data['publicTransport'] == "4-6":
        transporte -= 20
    elif data['publicTransport'] == "7+":
        transporte -= 30
    if data['bikeWalk'] == "Sim":
        transporte -= 15
    impacto_total += max(transporte, 10)

    # Energia
    energia = 40 if data['electricityBill'] > 500 else 20
    if data['efficientAppliances'] == "Sim":
        energia -= 10
    if data['solarPanels'] == "Sim":
        energia -= 20
    impacto_total += max(energia, 10)

    # Resíduos
    residuos = 30 if data['trashBags'] == "7+" else 15
    if data['recycle'] == "Não":
        residuos += 25
    impacto_total += max(residuos, 10)

    # Estilo de vida
    estilo_de_vida = 40 if data['shopping'] == "Muito" else 20
    if data['deliveries'] == "Muito":
        estilo_de_vida += 30
    impacto_total += max(estilo_de_vida, 10)

    # Alimentação e Água
    alimentacao = 0
    if data['meatConsumption'] == "Diariamente":
        alimentacao += 30
    elif data['meatConsumption'] == "3-4 vezes por semana":
        alimentacao += 20
    elif data['meatConsumption'] == "Raramente":
        alimentacao += 10
    if data['organicFood'] == "Sempre":
        alimentacao -= 10
    elif data['organicFood'] == "Às vezes":
        alimentacao -= 5
    if data['waterUsage'] == "3L+":
        alimentacao += 20
    elif data['waterUsage'] == "1-3L":
        alimentacao += 10
    elif data['waterUsage'] == "0-1L":
        alimentacao += 5

    impacto_total += alimentacao

    return round(impacto_total, 2)
