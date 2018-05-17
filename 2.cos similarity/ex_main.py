
# -*- coding: utf-8 -*-

if __name__=="__main__":
    import numpy as np
    from cosine_sim import cos
    
    sent1 = 'I am going to school .'
    sent2 = 'I ate dinner .'
    
    # 1. 단어 리스트 ['I', 'am', 'going', 'to', 'school', 'I', 'ate', 'dinner' '.' ] 만들기 
    
    # 2-1. vocabulary 리스트 ['I', 'am', 'going', 'to', 'school', 'ate', 'dinner' '.' ] 만들기 (!: 중복 없어야 함)
    
    # 2-2. vocabulary 사전 {'I':0, 'am':1, 'going':2 ...} 만들기 (!: 사전 has_key()함수 이용)
    
    # 3. 2-1혹은 2-2를 사용하여 문장에 들어있는 단어로 문장 벡터 만들기 (sent_vec1: [1 1 1 1 1 0 0], sent_vec2: [1 0 0 0 0 1 1])
    
    # 4. 유사도 계산 
    print 'The similarity is ', cos(sent_vec1, sent_vec2) 
    
    
