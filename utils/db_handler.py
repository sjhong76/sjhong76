# sjhong76/utils/db_handler.py
class DBHandler:
    def __init__(self):
        pass

    async def get_user_portfolio(self, user_id: str):
        """유저의 수익률 상태를 조회합니다."""
        # 실무 포인트: 손실률이 높을 경우 시스템 프롬프트에 '위로 가중치'를 부여하게 됩니다.
        return {
            "user_id": user_id,
            "status": "loss", 
            "loss_rate": -15.2, # 15% 손실 상태 가정
            "holdings": ["삼성전자", "현대차"]
        }