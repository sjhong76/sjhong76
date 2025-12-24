import re

def normalize_dob(text):
    """어떤 형식이든 YYMMDD 6자리로 변환"""
    numbers = re.sub(r'[^0-9]', '', text)
    if len(numbers) == 8: # 19761005 -> 761005
        return numbers[2:]
    elif len(numbers) == 6:
        return numbers
    return None

def parse_user_profile(message):
    """이름과 생년월일 추출 (간이 로직)"""
    # 실무에서는 LLM을 쓰거나 정규식을 더 보강합니다.
    dob = normalize_dob(message)
    # 이름은 '홍길동' 처럼 2~4자 한글 가정
    name_match = re.search(r'[가-힣]{2,4}', message)
    name = name_match.group() if name_match else None
    
    return name, dob