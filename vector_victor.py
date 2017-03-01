class ShapeError(Exception):
    pass


def shape(object):
    return (len(object),)


def vector_add(vector1, vector2):
    if len(vector1) == len(vector2):
        return [sum(pair) for pair in zip(vector1, vector2)]
    raise ShapeError


def vector_sub(vector1, vector2):
    if len(vector1) == len(vector2):
        return [vector1[i] - vector2[i] for i in range(len(vector1))]
    raise ShapeError


def dot(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ShapeError
    product_list = []
    # for i in range(len(vector1)):
    #     product_list.append(vector1[i] * vector2[i])
    # return sum(product_list)
    [product_list.append(vector1[i] * vector2[i]) for i in range(len(vector1))]
    return sum(product_list)


def vector_sum(*args):
    vectors = []
    [vectors.append(len(arg) == len(args[0])) for arg in args]
    if not sorted(vectors)[0]:
        raise ShapeError
    # my_list = []
    # for item in list(zip(*args)):
    #     my_list.append(sum(item))
    # return my_list
    my_list = list(zip(*args))
    new_list = []
    [new_list.append(sum(item)) for item in my_list]
    return new_list


def vector_multiply(vector, scalar):
    return [vector[i] * scalar for i in range(len(vector))]


def vector_mean(*args):
    totals = vector_sum(*args)
    return [totals[i] / len(args) for i in range(len(totals))]


def magnitude(vector):
    squared_vector = []
    [squared_vector.append(item ** 2) for item in vector]
    return sum(squared_vector) ** 0.5
