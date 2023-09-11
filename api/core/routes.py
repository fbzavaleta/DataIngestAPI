from flask import Blueprint, jsonify
from api.core.enums.http_status import  HttpStatus
from api.core.response.types import PayloadResponse


bp = Blueprint('core',__name__)
bp_v1 = Blueprint('status',__name__)

api_payload = {
    'apiversion' : 'v1',
    'owner' : 'fiap'
}

@bp.route('/ingest', methods=['POST'])
def ingest():
    #TODO: Realizar a implementação da lógica para a captura dinamica de dados.
    return jsonify(api_payload)

@bp.route('/read', methods=['GET'])
def read():
    #TODO: Realizar a implementação da lógica para o envio dinamico dos dados
    return jsonify(api_payload)

