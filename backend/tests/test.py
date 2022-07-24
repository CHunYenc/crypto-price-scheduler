import sys
import unittest

from app.extensions import make_redis
from app.tasks import get_binance_tickers
from . import BaseTestCase, logger


class Test(BaseTestCase):
    def test_create_app(self):
        app = self.create_app()
        client = app.test_client()
        response = client.get('/')
        logger.info(f'data = {response.data}')
        self.assertEqual(response.status_code, 200)
        assert b'test' in response.data

    def test_views_symbol_price(self):
        sys.setrecursionlimit(3000)
        app = self.create_app()
        r = make_redis(app)
        get_binance_tickers(r)
        # client = app.test_client()
        # response = client.get('/binance/btc/usdt')
        # logger.info(f'data = {response.data}')


if __name__ == '__main__':
    unittest.main()
