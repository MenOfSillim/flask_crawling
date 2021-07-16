# 파이썬 가상환경 라이브러리 설치 목록

```shell
    # 가상환경 설정
    - Mac : python3 -m venv_window ./(가상환경 설정할 디렉토리 이름)
    - Window : virtualenv flask_mongoDB
    
    # 가상환경 실행
    - Window : activate.bat | deactivate.bat
    - Mac : source (가상환경 디렉토리 이름)/bin/activate
    
    # 플라스크 설치
    pip install flask
    
    # pip 업그레이드
    python3 -m pip install --upgrade pip
    
    # Requests 설치
    pip install requests
    
    # 크롤링 설정 
    pip install bs4 
```

# MongoDB 설치

- Window 버전 [설치 가이드](https://scribblinganything.tistory.com/195)
    - MongoDB Compass 미설치 필요 : 에러 많음
    - robomongo로 관리
    - Dbeaver NoSQL은 EE버전을 설치해야 하는데, 유료 버전임 => [링크 확인](https://dbeaver.com/buy/lite/)


# Python -> MongoDB 연동
```shell
    pip install pymongo
```