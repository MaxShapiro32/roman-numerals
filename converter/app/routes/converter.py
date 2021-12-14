from app.services import data_handler
from app.errors import example_error
from app.jaeger import Jaeger
from flask import jsonify, request, Blueprint
from datetime import datetime
from pybreaker import CircuitBreaker

converter_blueprint = Blueprint("converter_blueprint", __name__)

breaker = CircuitBreaker(fail_max=5, reset_timeout=30)

context = Jaeger()


@converter_blueprint.route("/", methods=["GET"])
def converter():
    """
    /**
    * GET /api/v1/converter
    * @description Example route
    * @response 200 - OK
    * @response 400 - Error
    */
    """

    context.start("converter", request)
    try:
        data = breaker.call(data_handler.get_data, context)
        status_code = 200
    except Exception as e:
        data = {"error": e.args[0]}
        status_code = 400
    finally:
        context.stop(status_code)
        return jsonify(data), status_code
