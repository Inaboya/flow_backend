import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from src.schema import schema

def create_app() -> FastAPI:
    app = FastAPI(
        title="Reconciliation Engine",
        description="Python 3.13 Heuristic Scoring Service",
        version="1.0.0"
    )

    # 1. Setup CORS (Essential for NestJS to call this service)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], # In production, restrict this to your NestJS URL
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 2. Add GraphQL Router
    # The 'graphql' endpoint will host the Strawberry interface
    graphql_app = GraphQLRouter(schema)
    app.include_router(graphql_app, prefix="/graphql")

    # 3. Simple REST Health Check
    @app.get("/health")
    async def health():
        return {"status": "online", "engine": "Python 3.13", "framework": "FastAPI"}

    return app

app = create_app()

if __name__ == "__main__":
    # Port 8000 is standard to avoid conflict with NestJS (3000)
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)