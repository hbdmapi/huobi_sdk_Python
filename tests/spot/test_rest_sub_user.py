import sys
import unittest

sys.path.append('../..')
from huobi.spot.rest.sub_user import SubUser
from huobi.utils.logger import logger
from tests.config import ACCESS_KEY, SECRET_KEY


class TestRestSubUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = SubUser(ACCESS_KEY, SECRET_KEY)

    def test_set_deduct_mode(self):
        result = self.api.set_deduct_mode(
            {'subUids': '357503278', 'deductMode': 'master'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_get_api_key_info(self):
        result = self.api.get_api_key_info({'uid': '357503278'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_get_uid(self):
        result = self.api.get_uid()
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_create(self):
        result = self.api.create(
            {'userList': [{'userName': 'pytestlong220111', 'note': 'note'}]})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_get_sub_user_list(self):
        result = self.api.get_sub_user_list()
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_management(self):
        result = self.api.management({'subUid': 357503278, 'action': 'unlock'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_get_state(self):
        result = self.api.get_state({'subUid': 357503278})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_set_tradable(self):
        result = self.api.set_tradable(
            {'subUids': '357503278', 'accountType': 'cross-margin', 'activation': 'activated'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_set_transferability(self):
        result = self.api.set_transferability(
            {'subUids': '357503278', 'transferrable': True})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_get_account_list(self):
        result = self.api.get_account_list(
            {'subUid': 357503278})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_generate_api_key(self):
        result = self.api.generate_api_key(
            {'otpToken': 'usdt', 'subUid': 357503278, 'note': 'note', 'permission': 'readOnly'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_modify_api_key(self):
        result = self.api.modify_api_key(
            {'subUid': 357503278, 'accessKey': '', 'permission': 'readOnly'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_delete_api_key(self):
        result = self.api.delete_api_key(
            {'subUid': 357503278, 'accessKey': ''})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_transfer(self):
        result = self.api.transfer(
            {'sub-uid': 357503278, 'currency': 'usdt', 'amount': 1, 'type': 'master-transfer-out'})
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_deposit_address(self):
        result = self.api.get_deposit_address(
            {'subUid': 357503278, 'currency': 'usdt'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_get_deposit(self):
        result = self.api.get_deposit(
            {'subUid': 357503278, 'currency': 'usdt'})
        logger.info(result)
        self.assertEqual(200, result['code'])

    def test_get_aggregate_balance(self):
        result = self.api.get_aggregate_balance()
        logger.info(result)
        self.assertEqual('ok', result['status'])

    def test_get_balance(self):
        result = self.api.get_balance({'sub-uid': 357503278})
        logger.info(result)
        self.assertEqual('ok', result['status'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
