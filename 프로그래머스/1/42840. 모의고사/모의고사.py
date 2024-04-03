def solution(answers):
    answer =  [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    sheets = [[]]
    total_len = len(answers)
    score = []

    for i, ans in enumerate(answer):
        sheet = ans * (total_len // len(ans)) + ans[:total_len % len(ans)]
        # print(sheet)
        diff = [ai == bi for ai, bi in zip(answers, sheet)]

        score.append(sum(diff))
        m = max(score)
        answer = [idx + 1 for idx, val in enumerate(score) if val == m]
    return answer