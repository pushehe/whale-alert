#from urllib2 import Request, urlopen, URLError
import requests
#import gdax
# get buy volume increase in percent
# get sell volume increase in percent
# get price of Sell/buy order


class PublicClient(object):

	def __init__(self, api_url = 'https://api.gdax.com/'):

		self.url = api_url.rstrip('/')

	def get_products(self):

		r = requests.get(self.url + '/products', timeout = 30)
		return r.json()

	def get_product_order_book(self, product_id, level = 1):


		"""
		Args:
			product_id(str): Product
			level (Optional[int]): order book leevel(1,2,3). Def. is 1.

		Returns:
			dict: Order book. Eksample for level 1:
				{
                    "sequence": "3",
                    "bids": [
                        [ price, size, num-orders ],
                    ],
                    "asks": [
                        [ price, size, num-orders ],
                    ]
                }

		"""

		params = {'level': level}
		r = requests.get(self.url + '/products/{}/book'.format(product_id), params=params, timeout=30)

		# r.raise_for_status()
		return r.json()

	def get_product_ticker(self, product_id):
	
		"""Snapshot about the last trade (tick), best bid/ask and 24h volume.
        **Caution**: Polling is discouraged in favor of connecting via
        the websocket stream and listening for match messages.
        Args:
            product_id (str): Product
        Returns:
            dict: Ticker info. Example::
                {
                  "trade_id": 4729088,
                  "price": "333.99",
                  "size": "0.193",
                  "bid": "333.98",
                  "ask": "333.99",
                  "volume": "5957.11914015",
                  "time": "2015-11-14T20:46:03.511254Z"
                }
    	"""
		r = requests.get(self.url + '/products/{}/ticker'.format(product_id), timeout=30)
        # r.raise_for_status()
		return r.json()

	def get_product_trades(self, product_id):
		""" List the lates trades for a product.

    	Args:
            product_id (str): Product
        Returns:
            list: Latest trades. Example::
                [{
                    "time": "2014-11-07T22:19:28.578544Z",
                    "trade_id": 74,
                    "price": "10.00000000",
                    "size": "0.01000000",
                    "side": "buy"
                }, {
                    "time": "2014-11-07T01:08:43.642366Z",
                    "trade_id": 73,
                    "price": "100.00000000",
                    "size": "0.01000000",
                    "side": "sell"
                }]
        """

		r = requests.get(self.url + '/products/{}/trades'.format(product_id), timeout=30)
        # r.raise_for_status()
		return r.json()

if __name__ == '__main__':
	test = PublicClient()
	product = test.get_product_ticker("BTC-EUR")
	print(product)