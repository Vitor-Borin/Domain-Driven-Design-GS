from flask import Blueprint, request, jsonify
from app.domain.models import calcular_pegada

api_bp = Blueprint('api', __name__)

@api_bp.route('/calcular', methods=['POST'])
def calcular():
    try:
        dados = request.json
        resultado = calcular_pegada(dados)

        sugestoes = []
        if dados['carTravel'] > 100:
            sugestoes.append("Considere reduzir o uso de transporte individual.")
        else:
            sugestoes.append("Continue utilizando meios de transporte sustentáveis.")
        if dados['recycle'] == "Não":
            sugestoes.append("Comece a reciclar regularmente para diminuir os resíduos.")
        else:
            sugestoes.append("Parabéns por reciclar regularmente!")
        if dados['waterUsage'] == "3L+":
            sugestoes.append("Reduza seu consumo diário de água para menos de 3 litros.")
        else:
            sugestoes.append("Ótimo trabalho! Seu consumo de água está dentro da média sustentável.")
        if dados['meatConsumption'] == "Diariamente":
            sugestoes.append("Considere reduzir o consumo de carne para diminuir as emissões.")
        else:
            sugestoes.append("Seu consumo de carne está em níveis aceitáveis. Continue assim!")

        return jsonify({"impact": resultado, "sugestoes": sugestoes})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
