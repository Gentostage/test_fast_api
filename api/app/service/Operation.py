from ..models.common import Operations, ResultOperation

def get_operations_add(operaions: Operations) -> ResultOperation:
    return ResultOperation(result = operaions.number1 + operaions.number2)