from .base import *

# 데이터베이스 설정
DATABASES = SECRETS_JSON['DATABASES']['PRODUCTION']

# aws S3 설정
AWS_ACCESS_KEY_ID = SECRETS_JSON['AWS']['ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = SECRETS_JSON['AWS']['SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = SECRETS_JSON['AWS']['S3_BUCKET_NAME']
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'
AWS_QUERYSTRING_AUTH = False

# aws s3 저장소 설정
INSTALLED_APPS += ['storages']
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'
MEDIAFILES_LOCATION = 'media'
STATICFILES_LOCATION = 'static'

# s3 url 설정
MEDIA_URL = f'https://s3.ap-northeast-2.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/media/'
STATIC_URL = f'https://s3.ap-northeast-2.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/static/'

# debug false, 호스트 허용범위
DEBUG = False
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.ap-northeast-2.elasticbeanstalk.com',
    # 도메인 넣는다면 추가 '',
]

# aws beanstalk 헬스체크 허용
def is_ec2_linux():
    """Detect if we are running on an EC2 Linux Instance
       See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html
    """
    if os.path.isfile("/sys/hypervisor/uuid"):
        with open("/sys/hypervisor/uuid") as f:
            uuid = f.read()
            return uuid.startswith("ec2")
    return False


def get_linux_ec2_private_ip():
    """Get the private IP Address of the machine if running on an EC2 linux server"""
    from urllib.request import urlopen
    if not is_ec2_linux():
        return None
    try:
        response = urlopen('http://169.254.169.254/latest/meta-data/local-ipv4')
        ec2_ip = response.read().decode('utf-8')
        if response:
            response.close()
        return ec2_ip
    except Exception as e:
        print(e)
        return None

private_ip = get_linux_ec2_private_ip()
if private_ip:
    ALLOWED_HOSTS.append(private_ip)


# cors headers 실서버용
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
        '.ap-northeast-2.elasticbeanstalk.com',
        # 도메인 넣는다면 추가 '',
)
