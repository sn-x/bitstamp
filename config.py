redis_port = 6379

parameters  = {'start_amount_btc': 0.0021, # 0.019
               'start_amount_ltc': 0.21, # 1.9
#	       'start_amount_xrp': 56,
#	       'start_amount_eth': 0.04,
               'start_amount_eur': 15, # 95
               'start_amount_usd': 15, # 95
               'commision': 0.0025,  # 0.25%
               'adjustment': 0.00001 } # smallest value on b1tstamp?

conversions = {'btc': {'usd', 'eur'},
               'eur': {'usd'},
               'ltc': {'usd', 'eur', 'btc'} }
#	       'eth': {'usd', 'eur', 'btc'},
#	       'xrp': {'usd', 'eur', 'btc'}}

counters = {'success': {}, 'ratio': {}, 'highest_ratio':{} }

rounds = { 'btcusd': {'value': 2, 'amount': 8 },
           'btceur': {'value': 2, 'amount': 8 },
           'eurusd': {'value': 5, 'amount': 5 },
           'ltcusd': {'value': 2, 'amount': 8 },
           'ltceur': {'value': 2, 'amount': 8 },
           'ltcbtc': {'value': 8, 'amount': 8 } }

def fetchCurrencies():
	currencies = list()
        for currency in conversions:
		currencies.append(currency)
                for conversion in conversions[currency]:
			currencies.append(conversion)
	return set(currencies)

currencies = fetchCurrencies()


def buyDirections():
	buy = {}
	buy_2 = {}

	for quote in currencies:
		buy[quote] = {}
		list = []
		for base in conversions:
			if quote in conversions[base]:
				list.append(base)
		if list:
			buy.update({quote: tuple(list)})

	for currency in buy:
		if buy[currency]:
			buy_2.update({currency: buy[currency]})

	return buy_2

directions  = {'buy': buyDirections(),
	       'sell': conversions }
