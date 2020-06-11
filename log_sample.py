import logger
import logging as log

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
log.info('Add: {} + {} = {}'.format(num_1,num_2,add_result))

sub_result = subtract(num_1, num_2)
log.info('Sub: {} + {} = {}'.format(num_1,num_2,sub_result))

mul_result = multiply(num_1, num_2)
log.info('Multi: {} + {} = {}'.format(num_1,num_2,mul_result))

div_result = divide(num_1, num_2)
log.info('Div: {} + {} = {}'.format(num_1,num_2,div_result))

log.debug("This is a debug log")
log.info("This is a info log")
log.warning("This is a warning log")
log.error("This is a error log")
log.critical("This is a critical log")
