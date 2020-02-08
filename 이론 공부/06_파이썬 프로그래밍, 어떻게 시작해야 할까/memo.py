import sys

#cmd에서 아래와 같은 명령문을 통해 txt 파일 관리
# 추가 모드 이용 -> memo.py -a "추가내용"
# 읽기 모드 이용 -> memo.py -v

# sys.argv는 프로그램 실행 시 입력된 값들을 읽어 들일 수 있는 파이썬 라이브러리이다.
option = sys.argv[1]  # 옵션값

if option == '-a':  # 추가 모드
    memo = sys.argv[2]  # 메모 내용
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':  # 읽기 모드
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
