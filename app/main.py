from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .routers import authors, books, members
import uvicorn

# Create FastAPI application
app = FastAPI(
    title="Library Management System",
    description="A comprehensive library management system built with FastAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(authors.router, prefix="/api/v1")
app.include_router(books.router, prefix="/api/v1")
app.include_router(members.router, prefix="/api/v1")

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to Library Management System API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "library-management-api"}

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred"}
    )

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

