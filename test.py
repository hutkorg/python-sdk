from payment_provider import Api, Checkout

api = Api(merchant_id=1700001,
          secret_key='test',
          api_protocol='2.0',
          api_domain='pay.hutko.org')  # json - is default
checkout = Checkout(api=api)
data = {
    "preauth": 'N',
    "currency": "UAH",
    "amount": 20000,
    "reservation_data": {
        'key': 100,
        'key2': 200
    }
}
response = checkout.url(data)
print(response)
