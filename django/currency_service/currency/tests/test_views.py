class TestConverterView:

    def test_should_convert_to_new_currency(self, client):
        response = client.post(
            '/currency/brl/converter/usd/',
            data={'value': '10.00'}
        )
        assert response.status_code == 200
        assert response.data['id'] == 'USD'
        assert response.data['value']

    def test_should_return_bad_request_with_invalid_data(self, client):
        response = client.post(
            '/currency/brl/converter/usd/',
            data={}
        )
        assert response.status_code == 400
