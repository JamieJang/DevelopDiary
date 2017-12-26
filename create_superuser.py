import django
django.setup()

from django.contrib.auth import get_user_model

def main():
    username = 'admin'
    email = ''
    password = 'wkdwldyd1!'
    User = get_user_model()
    if not User.objects.filter(username=username).exists():
        # 로그인 후에 비밀번호를 필히 변경해주세요.
        User.objects.create_superuser(username, email, password)
        print('Sucessfully create superuser')

if __name__ == '__main__':
    main()

