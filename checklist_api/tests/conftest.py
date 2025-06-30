from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from checklist_api.database import get_session
from checklist_api.main import app
from checklist_api.models import User, table_registry


@pytest.fixture
def client(session):
    def get_session_override():
        return session
    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={
            'check_same_thread': False,
            'isolation_level': None
            },
        poolclass=StaticPool,
        pool_pre_ping=True,
        echo=False)

    table_registry.metadata.create_all(engine)

    try:
        with Session(engine) as session:
            yield session
    finally:
        table_registry.metadata.drop_all(engine)
        engine.dispose()


@contextmanager
def _mock_db_time(*, model, time=datetime(2025, 1, 1)):

    def fake_time_hook(mapper, connection, target):
        if hasattr(target, 'created_at'):
            target.created_at = time

    event.listen(model, 'before_insert', fake_time_hook)

    yield time

    event.remove(model, 'before_insert', fake_time_hook)


@pytest.fixture
def mock_db_time():
    return _mock_db_time


@pytest.fixture
def user(session):
    user = User(username='Teste', email='teste@test.com', password='testtest')
    session.add(user)
    session.commit()
    session.refresh(user)

    return user
