# backend/routers/analyze.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


# 요청 본문(Request Body) 모델
# 손님이 제출하는 주문서 양식
class AnalyzeRequest(BaseModel):
    major: str          # 전공 (예: "통계학과")
    skills: List[str]   # 보유 스킬 목록 (예: ["Python", "SQL"])
    job_type: str       # 관심 직무 (예: "데이터 분석")


# 응답 본문(Response Body) 모델
# 주방에서 손님에게 돌려주는 영수증 양식
class AnalyzeResponse(BaseModel):
    answer: str         # AI 분석 결과 텍스트
    sources: List[dict] # 답변 근거 데이터 목록


@router.post("/analyze", response_model=AnalyzeResponse, tags=["Analyze"])
def analyze_career(request: AnalyzeRequest):
    """
    사용자의 전공·스킬·관심 직무를 기반으로 취업·공모전 맞춤 분석을 제공한다.
    현재는 목업 응답을 반환하며, 실습 8에서 Gemini API와 연결한다.
    """
    # 임시 목업 응답: 실습 8에서 실제 Gemini + RAG 응답으로 교체한다
    mock_answer = (
        f"{request.major} 전공자로서 {request.job_type} 직무를 준비하려면, "
        f"현재 보유한 {', '.join(request.skills)} 역량을 기반으로 "
        f"채용 공고에서 자주 요구되는 Python, FastAPI, 데이터 처리 역량을 강화하는 것이 좋습니다. "
        f"특히 AI 서비스 엔지니어를 목표로 한다면 LLM API 활용, 백엔드 API 설계, "
        f"프로젝트 결과를 설명할 수 있는 포트폴리오 정리가 중요합니다. "
        f"(목업 응답 — 실습 8에서 Gemini로 교체)"
    )

    mock_sources = [
        {
            "title": "목업 데이터 — 네이버클라우드 AI 서비스 엔지니어",
            "content": "요구 스킬: Python, FastAPI, LLM API",
        },
        {
            "title": "목업 데이터 — 카카오페이 데이터 분석가",
            "content": "요구 스킬: Python, SQL, Pandas",
        },
        {
            "title": "목업 데이터 — 현대오토에버 백엔드 개발자",
            "content": "요구 스킬: Python, FastAPI, SQLite",
        },
    ]

    return AnalyzeResponse(answer=mock_answer, sources=mock_sources)