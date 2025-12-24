# LUA (Lazy User Agent) 🌙
> **"복잡함은 AI가, 당신은 대화만"** - 채팅형 주식 트레이딩 플랫폼

## 🛠 Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python (FastAPI logic)
- **AI**: OpenAI (GPT-4o-mini)
- **Database/Search**: MongoDB, Elasticsearch (Planned)

## 🚀 How to Run
1. 라이브러리 설치: `pip install -r requirements.txt`
2. 환경 변수 설정: `.env` 파일에 `OPENAI_API_KEY` 입력
3. 실행: `streamlit run lua.py`

sjhong76/
├── lua.py               # [Main] 대시보드 타이틀, 3년 주봉, 채팅 레이아웃
├── requirements.txt     # [Install] 필수 라이브러리 목록
├── .gitignore           # [Security] 보안 제외 설정
├── agent/
│   └── lua_core.py      # [Logic] LUA 페르소나 및 아저씨 코멘트 생성
└── utils/
    ├── parser.py        # [Logic] 날짜 및 이름 파싱 정규식
    └── db_handler.py    # [Data] 계좌 미확인 테스트용 핸들러
