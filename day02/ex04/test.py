import ai42.logging.log


@ai42.logging.log.log
def function(x, y):
    x = x * y
    y = y ** 2
    return x + y
