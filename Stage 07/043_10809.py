main_str = input()
alphabet = list(range(97, 123))

# 알파벳은 소문자로만 구성
# 소문자 a ~ z는 97 ~ 122의 값이다. (ASCII)
# 각 알파벳 별로 순차적으로 검색, 하나라도 발견되면 continue로 다음 루프로 전환
for ascii_num in alphabet:
    print(main_str.find(chr(ascii_num)))