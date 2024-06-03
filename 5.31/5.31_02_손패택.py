'''
2024년05월31일
202195057 손패택

[문제분석]
코드는 먼저 사용자로부터 정수를 얻어 변수 num에 저장합니다.
그런 다음 모듈러 연산자 %를 사용하여,
num%2의 나머지를 확인하고 나머지가 0이면 짝수입니다.
반대로 홀수, 
뒤이어 프로그램이 결과를 출력합니다.

[알고리즘]

'''
#두 숫자의 합을 반환하는 함수 생성.
def check_even_ood(number):
    if number % 2 == 0:
        return "짝수"
    else :
        return "홀수"
    #메인
num = int(input("수자 를 입력하시오:"))
result = check_even_ood(num)
print(f"{num}를 {result}.")