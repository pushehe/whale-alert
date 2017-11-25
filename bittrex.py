import requests

BUY_ORDERBOOK = 'buy'
SELL_ORDERBOOK = 'sell'
BOTH_ORDERBOOK = 'both'

class PublicBittrexAPI(object):

	def __init__(self, api_url = 'https://bittrex.com/api/v1.1/public/'):

		self.url = api_url.rstrip('/')

	def get_markets(self):

		"""
        Used to get the open and available trading markets
        at Bittrex along with other meta data.
        :return: Available market info in JSON
        :rtype : dict

        Example ::
            {'success': True,
             'message': '',
             'result': [ {'MarketCurrency': 'LTC',
                          'BaseCurrency': 'BTC',
                          'MarketCurrencyLong': 'Litecoin',
                          'BaseCurrencyLong': 'Bitcoin',
                          'MinTradeSize': 1e-08,
                          'MarketName': 'BTC-LTC',
                          'IsActive': True,
                          'Created': '2014-02-13T00:00:00',
                          'Notice': None,
                          'IsSponsored': None,
                          'LogoUrl': 'https://i.imgur.com/R29q3dD.png'},
                          ...
                        ]
            }

        """

		r = requests.get(self.url + '/getmarkets', timeout = 30)
		return r.json()

	def get_currencies(self):

		# fetches all supported currencies at Bittrex aling with other metadata
		# Returns: Supported currencies in JSON
		# Return type: dictionary {}

		r = requests.get(self.url + '/getcurrencies', timeout = 30)
		return r.json()

	def get_ticker(self, market):

		"""
        Used to get the current tick values for a market.
        Endpoints:
        :param market: String literal for the market (ex: BTC-LTC)
        :type market: str
        :return: Current values for given market in JSON
        :rtype : dict
        """

		r = requests.get(self.url + '/getticker?market={}'.format(market), timeout = 30)
		return r.json()

	def get_orderbook(self, market, depth_type=BOTH_ORDERBOOK):

		"""
        Used to get retrieve the orderbook for a given market.
        The depth_type parameter is IGNORED under v2.0 and both orderbooks are aleways returned
        Endpoint:
        :param market: String literal for the market (ex: BTC-LTC)
        :type market: str
        :param depth_type: buy, sell or both to identify the type of
            orderbook to return.
            Use constants BUY_ORDERBOOK, SELL_ORDERBOOK, BOTH_ORDERBOOK
        :type depth_type: str
        :return: Orderbook of market in JSON
        :rtype : dict
        """

		r = requests.get(self.url + '/getorderbook?market={}&type={}'.format(market, depth_type), timeout = 30)
		return r.json()

	def get_market_trades(self, market):

		"""
        Used to retrieve the latest trades that have occurred for a
        specific market.
        Endpoint:
        Example ::
            {'success': True,
            'message': '',
            'result': [ {'Id': 5625015,
                         'TimeStamp': '2017-08-31T01:29:50.427',
                         'Quantity': 7.31008193,
                         'Price': 0.00177639,
                         'Total': 0.01298555,
                         'FillType': 'FILL',
                         'OrderType': 'BUY'},
                         ...
                       ]
            }
        :param market: String literal for the market (ex: BTC-LTC)
        :type market: str
        :return: Market history in JSON
        :rtype : dict
        """

		r = requests.get(self.url + '/getmarkethistory?market={}'.format(market), timeout = 30)
		return r.json()

if __name__ == '__main__':
	test = PublicBittrexAPI()
	product = test.get_ticker("BTC-LTC")
	print(product)




