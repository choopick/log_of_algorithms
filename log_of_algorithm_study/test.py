class User:
    def say_hello(some_user):
        #인사 메세지 출력 메소드
        print("안녕하세요! 저는 {}입니다!".format(some_user.name))

    def login(some_user, my_email, my_password):
        #로그인 메소드
        if (some_user.email == my_email and some_user.password == my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호 입니다.")

user1 = User()

user1.name = "김대위"
user1.email = "captain@codeit.co.kr"