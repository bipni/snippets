import grpc
from concurrent import futures
import time

import calculator_pb2
import calculator_pb2_grpc

import calculator

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response