"""
SmartShop AI Backend - Dependency Injection Module

Provides FastAPI dependency injection setup for services, repositories, and utilities.
"""

from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.cache.redis_client import RedisClient, get_redis_client
from app.repositories.product_repository import ProductRepository
from app.services.search_service import SearchService
from app.services.comparison_service import ComparisonService
from app.services.recommendation_service import RecommendationService
from app.services.aggregation_service import AggregationService
from app.ml.query_parser import QueryParser
from app.ml.embeddings import EmbeddingGenerator
from app.ml.similarity import SimilarityEngine
from app.ml.ranking import RankingEngine
from app.ml.summarizer import Summarizer


# Repository Dependencies
def get_product_repository(db: Session = Depends(get_db)) -> ProductRepository:
    """Get product repository instance"""
    return ProductRepository(db)


# ML Component Dependencies
def get_query_parser() -> QueryParser:
    """Get query parser instance"""
    return QueryParser()


def get_embedding_generator() -> EmbeddingGenerator:
    """Get embedding generator instance"""
    return EmbeddingGenerator()


def get_similarity_engine() -> SimilarityEngine:
    """Get similarity engine instance"""
    return SimilarityEngine()


def get_ranking_engine() -> RankingEngine:
    """Get ranking engine instance"""
    return RankingEngine()


def get_summarizer() -> Summarizer:
    """Get summarizer instance"""
    return Summarizer()


# Service Dependencies
def get_search_service(
    db: Session = Depends(get_db),
    redis: RedisClient = Depends(get_redis_client),
    query_parser: QueryParser = Depends(get_query_parser),
    embedding_gen: EmbeddingGenerator = Depends(get_embedding_generator),
    similarity_engine: SimilarityEngine = Depends(get_similarity_engine),
    ranking_engine: RankingEngine = Depends(get_ranking_engine)
) -> SearchService:
    """Get search service instance with all dependencies"""
    return SearchService(
        db=db,
        redis=redis,
        query_parser=query_parser,
        embedding_gen=embedding_gen,
        similarity_engine=similarity_engine,
        ranking_engine=ranking_engine
    )


def get_comparison_service(
    db: Session = Depends(get_db),
    redis: RedisClient = Depends(get_redis_client)
) -> ComparisonService:
    """Get comparison service instance"""
    return ComparisonService(db=db, redis=redis)


def get_recommendation_service(
    db: Session = Depends(get_db),
    similarity_engine: SimilarityEngine = Depends(get_similarity_engine),
    ranking_engine: RankingEngine = Depends(get_ranking_engine)
) -> RecommendationService:
    """Get recommendation service instance"""
    return RecommendationService(
        db=db,
        similarity_engine=similarity_engine,
        ranking_engine=ranking_engine
    )


def get_aggregation_service(
    redis: RedisClient = Depends(get_redis_client)
) -> AggregationService:
    """Get aggregation service instance"""
    return AggregationService(redis=redis)
