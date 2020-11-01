def test_weather(client):
    city = 'Guadalajara'
    response = client.get("/weather/" + city )
    assert b'weather' in response.data