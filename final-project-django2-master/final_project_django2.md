# research 모델을 짜보자. => preference

## 0. 모델의 목적

- User : Preference = 1 : 1 => 각 유저는 하나의 선호도를 가짐
- Movie : Characteristic(Preference) = 1 : 1 => 각 영화는 하나의 특성을 가짐
- User의 Preference와 Movie의 Characteristic 의 속성들을 하나씩 비교하면서 추천도 값을 작성
- User의 초기 선택과 이후 추천 영화 선택에 따라 Preference값은 조정

## 1. 속성

- 영화명(movieNm)

- 제작연도(prdtYear)
- 상영시간(showTm)
- 제작국가(nationNm)
- 장르(genreNm)
- 감독(directors)
- 배우(actors)
- 관람등급(watchGradeNm)



## 2. heroku 배포

- git 따라감
- deploy: 로컬에 있는 서버를 외부로 옮겨가는 것
  - SSH, FTP: 요즘 이거는 잘 안씀
  - git에서 코드를 관리하고 있기 때문에 git remote respository(gitlab, github) 에서 clone, pull을 받아서 서버에 적용하는 방식이 제일 일반적

- settings.py

  ```python
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  ```

- python manage.py collectstatic: 스태틱 파일을 모아줌

- .gitignore

  ```
  # 배포용 ignore
  venv
  *.sqlite3
  .env
  *.bak
  ```

- 애드, 커밋, 푸시 해줌

- . env에 settings.py에 있는 키 복사 입력, DEBUG=True

  ```
  SECRET_KEY='7lf$fcq-ri-cryh(+1gcgj1yq0vi#qabb(mz0yu05h=t$5b4g='
  DEBUG=True
  ```

  ```python
  from decouple import config
  
  SECRET_KEY = config('SECRET_KEY')
  DEBUG = config('DEBUG')
  ```

- heroku 가입, heroku cli 64비트 다운, 설치!
- heroku, heroku login
- heroku create, heroku create 이름: 컴퓨터를 하나 만듦
- git remote -v => 해당 컴퓨터에 들어가서 settings에서 key, value 등록

- runtime.txt
- procfile
- pip install gunicorn

- pip freeze > requirements.txt

- 애드, 커밋, 푸시

- git push heroku master

- settings.py

  ```python
  ALLOWED_HOSTS = [
      'ancient-lake-51221.herokuapp.com',
  ]
  ```

- heroku run python manage.py makemigrations

- 해당 컴퓨터 more의 콘솔에서 python manage.py migrate

- heroku git:remote -a ssafy-jjang2

- pip install django-heroku

- settings.py

  ```python
  import django_heroku
  
  django_heroku.settings(locals())
  ```
- makemigrations까지 하고나서 해로쿠 푸시하고, 콘솔에서 migrate하고, 배포 사이트 이용하면 됨!