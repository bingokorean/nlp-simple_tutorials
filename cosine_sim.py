def cos(v1,v2):

    return numpy.dot(v1,v2)/((numpy.sqrt(numpy.dot(v1,v1))*numpy.sqrt(numpy.dot(v2,v2)))+0.000000001)
