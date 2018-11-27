#-*- encoding:utf-8 -*-

def cos(v1,v2):
    import numpy as np
    return np.dot(v1,v2)/((np.sqrt(np.dot(v1,v1))*np.sqrt(np.dot(v2,v2)))+np.finfo(float).eps)

    
