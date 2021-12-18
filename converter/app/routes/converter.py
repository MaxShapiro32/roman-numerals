from app.services import data_handler
from app.errors import roman_numeral_error
from app.jaeger import Jaeger
from flask import jsonify, request, Blueprint, Response
from datetime import datetime
from pybreaker import CircuitBreaker

converter_blueprint = Blueprint("converter_blueprint", __name__)

breaker = CircuitBreaker(fail_max=5, reset_timeout=30)

context = Jaeger()


@converter_blueprint.route("/to-roman", methods=["GET"])
def to_roman():
    """
    /**
    * GET /api/v1/converter/to-roman
    * @description Converting Numbers to Roman Numerals
    * @queryParam {int} value - Number value
    * @response 200 - OK
    * @response 400 - Error
    */
    """

    context.start("to-roman", request)
    try:
        query_data = request.args
        data = breaker.call(data_handler.to_roman_numeral, _get_query_param("value", query_data, int))
        status_code = 200
    except Exception as e:
        data = e.args[0]
        status_code = 400
    finally:
        context.stop(status_code)
        return Response(response=data, status=status_code, content_type="text/plain")


@converter_blueprint.route("/to-number", methods=["GET"])
def to_number():
    """
    /**
    * GET /api/v1/converter/to-number
    * @description Converting Roman Numerals to Numbers
    * @queryParam {int} value - Roman Numeral
    * @response 200 - OK
    * @response 400 - Error
    */
    """

    context.start("to-number", request)
    try:
        query_data = request.args
        data = breaker.call(data_handler.to_number, _get_query_param("value", query_data, str))
        status_code = 200
    except Exception as e:
        data = e.args[0]
        status_code = 400
    finally:
        context.stop(status_code)
        return Response(response=str(data), status=status_code, content_type="text/plain")


def _get_query_param(key, query_data, func):
    if key in query_data.keys():
        try:
            return func(query_data[key])
        except:
            raise roman_numeral_error.InvalidNumberException("Error: Invalid Number")
    raise roman_numeral_error.InvalidNumberException("Error: Invalid Number")
