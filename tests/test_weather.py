import json

def test_weather(client):
    response = client.get("/weather/Guadalajara/")
    assert response.status_code == 200
    assert is_json(response.data)
    assert b'clouds' in response.data

def is_json(data):
    str_resp = data.decode('utf-8')
    try:
        json.loads(str_resp)        
    except json.decoder.JSONDecodeError as e:
        return False
    return True