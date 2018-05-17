
# -*- coding: utf-8 -*-

if __name__=="__main__":
    import numpy as np
    from cosine_sim import cos
    data = [u'안녕 나는 오늘 밥을 먹었어',
              u"나는 나는 오늘 학교에 안가기로 했어"]
    vocab_dic = dict([(w,i) for i,w in enumerate(list(set(' '.join(data).split())))])
    v1 = np.zeros(len(vocab_dic))
    v2 = np.zeros(len(vocab_dic))

    for w in data[0].split():   #첫번째 문장 벡터 (binary)
        v1[vocab_dic[w]] = 1

    for w in data[1].split():   #두번째 문장 벡터 (binary)
        v2[vocab_dic[w]] = 1

    print 'The similarity of [', data[0] , '] and [', data[1], '] is:'
    print cos(v1,v2)
