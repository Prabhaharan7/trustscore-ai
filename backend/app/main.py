from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.assessments import router as assessments_router
from app.routes.attempts import router as attempts_router

app = FastAPI(
    title="TrustScoreAI",
    description="AI-based assessment platform API",
    version="1.0.0",
)

# Add CORS middleware (allow all origins for hackathon)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(users_router, prefix="/api/users", tags=["Users"])
app.include_router(assessments_router, prefix="/api/assessments", tags=["Assessments"])
app.include_router(attempts_router, prefix="/api/attempts", tags=["Attempts"])

@app.get("/health", tags=["Health"])
async def health_check():
    """Simple health check route."""
    return {"status": "ok"}
