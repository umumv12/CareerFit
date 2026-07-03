# backend/routers/jobs.py
from fastapi import APIRouter, HTTPException

router = APIRouter()

# 목업 데이터: 3일차에 실제 CSV 데이터로 교체한다
MOCK_JOBS = [
    {
        "id": 1,
        "company": "네이버클라우드",
        "title": "AI 서비스 엔지니어",
        "required_skills": ["Python", "FastAPI", "LLM API"],
        "preferred_skills": ["Docker", "RAG", "클라우드 배포"],
        "description": "생성형 AI API를 활용한 서비스 기능을 개발하고 백엔드 API와 연동합니다. 사용자 요청을 분석해 적절한 AI 응답을 제공하는 기능을 설계합니다.",
        "deadline": "2026-08-31",
    },
    {
        "id": 2,
        "company": "카카오페이",
        "title": "데이터 분석가",
        "required_skills": ["Python", "SQL", "Pandas"],
        "preferred_skills": ["Tableau", "통계 분석", "머신러닝"],
        "description": "서비스 이용 데이터를 분석해 사용자 행동 패턴과 비즈니스 인사이트를 도출합니다. 분석 결과를 바탕으로 서비스 개선 방향을 제안합니다.",
        "deadline": "2026-08-31",
    },
    {
        "id": 3,
        "company": "현대오토에버",
        "title": "백엔드 개발자",
        "required_skills": ["Python", "FastAPI", "SQLite"],
        "preferred_skills": ["Docker", "AWS", "API 설계"],
        "description": "데이터 기반 서비스의 백엔드 API를 개발하고 안정적으로 운영합니다. 프론트엔드와 연동되는 서버 기능을 구현하고 데이터 처리 로직을 관리합니다.",
        "deadline": "2026-08-31",
    },
]


@router.get("/jobs", tags=["Jobs"])
def get_jobs():
    """
    취업 공고 목록을 반환하는 엔드포인트.
    현재는 목업 데이터를 반환하며, 3일차에 실제 데이터로 교체한다.
    """
    return {
        "count": len(MOCK_JOBS),
        "jobs": MOCK_JOBS,
    }


@router.get("/jobs/{job_id}", tags=["Jobs"])
def get_job_by_id(job_id: int):
    """
    특정 공고의 상세 정보를 반환한다.
    """
    for job in MOCK_JOBS:
        if job["id"] == job_id:
            return job

    raise HTTPException(status_code=404, detail=f"공고 ID {job_id}를 찾을 수 없습니다.")