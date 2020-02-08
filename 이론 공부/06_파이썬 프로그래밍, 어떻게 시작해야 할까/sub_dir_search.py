import os


def search(dirname):
    try:
        filenames = os.listdir(dirname)  # os.listdir을 이용하면 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있다. 경로를 포함하지 않은 파일명.
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)  # 경로(디렉터리와 파일명)를 합쳐준다.
            if os.path.isdir(full_filename):  # 파일인지 디렉터리인지 구분
                search(full_filename)  # 디렉터리일 경우 다시 search 함수 호출
            else:
                ext = os.path.splitext(full_filename)[-1]  # 확장자 추출(os.path.splitext는 파일명을 확장자를 기준으로 두 부분으로 나누어 준다.)
                if ext == '.py':
                    print(full_filename)
    except PermissionError:  # os.listdir 수행 시 권한이 없는 디렉터리에 접근하더라도 프로그램이 오류로 종료되지 않고 그냥 수행되도록 하기 위해서 try, except 구분
        pass


def search2(dirname):  # os.walk 사용(시작 디렉터리부터 시작하여 그 하위의 모든 디렉터리를 차례대로 방문하게 해주는 함수이다.)
    for (path, dir, files) in os.walk(dirname):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.py':
                print("%s/%s" % (path, filename))


#search("C:/")
#search2("C:/")
