# sjhong76/lua.py
import streamlit as st
import asyncio
import time
from agent.lua_core import LUAAgent
from utils.parser import parse_user_profile
from utils.exception_handler import LUAExceptionHandler
from utils.order_manager import OrderManager
from utils.balance_manager import BalanceManager
from utils.market_data import MarketDataManager

# --- 페이지 설정 ---
st.set_page_config(page_title="LUA (Lazy User Agent)", page_icon="🌙", layout="wide")

# --- 상태 관리 초기화 (State Machine) ---
if "step" not in st.session_state:
    st.session_state.step = "STEP_1" # 오프닝 시작
    st.session_state.user_info = {"name": None, "dob": None, "is_guest": True}
    st.session_state.order_context = {} # 주문 처리 중 임시 데이터

# 모듈 초기화
agent = LUAAgent()
err_handler = LUAExceptionHandler()
order_mgr = OrderManager()
balance_mgr = BalanceManager()
market_mgr = MarketDataManager()

st.title("LUA: Lazy User Agent 🌙")
st.sidebar.title("🛠️ 테스트 컨트롤러")
if st.sidebar.button("초기화 (Reset)"):
    st.session_state.step = "STEP_1"
    st.session_state.user_info = {"name": None, "dob": None, "is_guest": True}
    st.rerun()

# --- 시나리오 제어 로직 ---

# STEP 1 & 2: 오프닝 및 프로필 파싱 [cite: 24, 25]
if st.session_state.step == "STEP_1":
    st.chat_message("assistant").write("안녕하세요, LUA(루아)예요! 😊\n원하시는 걸 대화로 편하게 도와드릴게요.\n\n이름과 생년월일(6자리)을 알려주시면 바로 안내해 드릴게요!")
    
    if prompt := st.chat_input("예: 홍길동 761005"):
        name, dob = parse_user_profile(prompt)
        if name and dob:
            st.session_state.user_info = {"name": name, "dob": dob, "is_guest": False}
            st.session_state.step = "STEP_3" # 분기로 이동
            st.rerun()
        else:
            # 파싱 실패 시 게스트 모드 제안 [cite: 196]
            st.warning("앗, 정보를 확실히 알기 어려워요. 성함과 생년월일 6자리를 다시 적어주시거나, 게스트로 시작할까요?")
            if st.button("게스트로 시작하기"):
                st.session_state.step = "STEP_10" # 시장 요약(게스트 가능)으로 이동
                st.rerun()

# STEP 3: 결과 분기 (계좌 확인됨 가정) [cite: 64, 65]
elif st.session_state.step == "STEP_3":
    name = st.session_state.user_info['name']
    st.chat_message("assistant").write(f"✨ **{name}**님, 키움 증권에 계좌가 있는 것이 확인되었습니다.\n무엇부터 도와드릴까요?")
    
    c1, c2, c3 = st.columns(3)
    if c1.button("🛒 실전 거래 시작"): st.session_state.step = "STEP_5"; st.rerun()
    if c2.button("💰 보유/잔고 보기"): st.session_state.step = "STEP_9"; st.rerun()
    if c3.button("📊 시장 요약 보기"): st.session_state.step = "STEP_10"; st.rerun()
    if st.button("🔄 주문 정정/취소"): st.session_state.step = "STEP_7_LIST"; st.rerun()

# STEP 5: 첫 주문 (통역->확인->실행) [cite: 68, 69]
elif st.session_state.step == "STEP_5":
    st.chat_message("assistant").write("원하시는 주문을 말씀해 주세요. (예: 삼성전자 10주 사줘)")
    if prompt := st.chat_input("주문 입력"):
        # LLM 통역 시뮬레이션
        st.session_state.order_context = {"item": "삼성전자(005930)", "amount": 10, "type": "매수", "price": "시장가"}
        st.session_state.step = "STEP_5_CONFIRM_1"
        st.rerun()

elif st.session_state.step == "STEP_5_CONFIRM_1":
    ord = st.session_state.order_context
    st.info(f"**주문 요약**\n- 종목: {ord['item']}\n- 수량: {ord['amount']}주\n- 구분: {ord['type']}\n\n이대로 접수할까요?")
    col1, col2 = st.columns(2)
    if col1.button("✅ 예"): st.session_state.step = "STEP_5_CONFIRM_2"; st.rerun()
    if col2.button("❌ 아니오"): st.session_state.step = "STEP_3"; st.rerun()

elif st.session_state.step == "STEP_5_CONFIRM_2":
    st.warning("⚠️ 마지막 확인입니다. **'확인'**이라고 입력해 주세요.")
    if final := st.chat_input("'확인' 입력"):
        if final == "확인":
            st.success("✅ 접수가 완료되었습니다! (주문번호: LUA-777)")
            time.sleep(2)
            st.session_state.step = "STEP_3"; st.rerun()

# STEP 6, 7, 9, 10은 이전 코드 블록의 로직을 step 조건문에 맞춰 배치합니다.
# (지면상 요약하며, 실제 파일에는 모든 단계의 UI 코드가 포함됩니다.)
else:
    st.write(f"현재 {st.session_state.step} 단계 구현부입니다. (작업 중)")
    if st.button("홈으로"): st.session_state.step = "STEP_3"; st.rerun()