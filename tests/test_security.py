from datetime import datetime, timedelta
from http import HTTPStatus
from zoneinfo import ZoneInfo

from jwt import decode, encode

from checklist_api.security import SECRET_KEY, create_access_token


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(token, SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert 'exp' in decoded


def test_jwt_invalid_token(client):
    response = client.delete(
        'users/1',
         headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {
        'detail': 'Could not validate credentials'}


def test_jwt_token_without_sub(client):
    token_data = {
        'user_id': 123,
        'exp': datetime.now(tz=ZoneInfo('UTC')) + timedelta(minutes=30)
    }
    token = encode(token_data, SECRET_KEY, algorithm='HS256')

    response = client.delete(
        'users/1',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_jwt_token_with_nonexistent_user(client):
    token_data = {
        'sub': 'usuario_inexistente@example.com',
        'exp': datetime.now(tz=ZoneInfo('UTC')) + timedelta(minutes=30)
    }
    token = encode(token_data, SECRET_KEY, algorithm='HS256')

    response = client.delete(
        'users/1',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
