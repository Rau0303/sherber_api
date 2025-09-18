import pytest


@pytest.mark.asyncio
async def test_register_user_success(async_client):
    phone = '77784476406'
    password = 'qwerty123'
    email = 'example@example.com'
    client = {
        'platform': 'ios',
        'os_version': '16.0',
        'app_version':'1.0.0',
        'app_build_version':'1',
        'locale':'ru-RU'

    }
    payload = {
        'phone': phone,
        'password': password,
        'email': email,
        'client': client
    }

    response = await async_client.post('/auth/register', json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data['status'] == 'success'
    assert data['data']['user']['phone'] == payload['phone']
    assert data['data']['user']['email'] == payload['email']





@pytest.mark.asyncio
async def test_register_user_conflict(async_client):
    phone = '77784476406'
    password = 'qwerty123'
    email = 'example@example.com'
    client = {
        'platform': 'ios',
        'os_version': '16.0',
        'app_version':'1.0.0',
        'app_build_version':'1',
        'locale':'ru-RU'

    }
    payload = {
        'phone': phone,
        'password': password,
        'email': email,
        'client': client
    }

    response = await async_client.post('/auth/register', json=payload)
    assert response.status_code == 409
    