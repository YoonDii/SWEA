# 어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.
# 이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.
# 다음과 같은 수 분포가 있으면,
# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
# 최빈수는 8이 된다.
# 최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).

# [제약 사항]
# 학생의 수는 1000명이며, 각 학생의 점수는 0점 이상 100점 이하의 값이다.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

import sys
sys.stdin = open('1204.txt',"r")

T = int(input())
for i in range(T):
    test_number = int(input())
    scores = list(map(int, input().split()))
    mode = 0  # 1 우리가 알고싶은 최빈수 값(mode) 변수를 만든다.

    # 2 최빈수 딕셔너리(dictionary)를 만든다. ex) 8이 2개, 4가 3개일 경우 {8:2, 4:3}
    count_dic = {}
    for i in scores:
        if i in count_dic:
            count_dic[i] += 1
        else:
            count_dic[i] = 1
    # 3 최빈수 딕셔너리를 숫자값(key)과 카운트값(value)을 items()로 꺼내와 for문을 돌린다.
    max_count = 0
    for key, value in count_dic.items():
        if max_count < value:  # 4 카운트값(value)이 최댓값(즉, 최빈수)일때 최빈수값(mode)에 숫자값(key)을 넣는다.
            max_count = value
            mode = key
        elif max_count == value:  # 5 꺼낸 카운트값이 최댓값과 같을 경우 숫자값을 비교하여 큰 숫자를 넣는다.
            if mode < key:
                mode = key
    # 6 최빈수 값(mode)을 출력한다.
    print('#{} {}'.format(test_number, mode))