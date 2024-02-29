from collections import Counter

def solution(s):
    result = len(s)
    # 반복 (나누는 단위 : length)
    for length in range(1, len(s)//2 + 1):
        # 같은 거 찾기
        answer = len(s)
        tmp = s[0:length]
        cnt = 1
        for i in range(0+length, len(s), length):
            now = s[i:i+length]
            if now == tmp:
                answer -= len(now)
                cnt += 1
            else:
                if cnt > 1:
                    answer += len(str(cnt))
                tmp = now
                cnt = 1
        if cnt > 1:
            answer += len(str(cnt))

        if answer < result:
            result = answer
    return result


##################################
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
