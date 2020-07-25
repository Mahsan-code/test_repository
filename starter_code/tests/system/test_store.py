from starter_code.models.item import ItemModel
from starter_code.models.store import StoreModel
from starter_code.tests.base_test import BaseTest
import  json

class StoreTest(BaseTest):

    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                request = client.post('/store/costco')
                self.assertEqual(request.satus_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('costco'))
                self.assertDictEqual({'name': 'test', 'item': []},
                                     json.loads(request.data))


    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                request = client.post('/store/costco')
                request2= client.post('/store/costco')
                self.assertEqual(request2.satus_code, 400)
                self.assertDictEqual({'message': 'A store with name costco already exists.'},
                                     json.loads(request.data))

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('costco').save_to_db()
                request = client.delete('/store/costco')
                self.assertIsNone(StoreModel.find_by_name('costco'))
                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'message': 'Store deleted'}, json.loads(request.data))



    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('costco').save_to_db()
                request = client.get('/store/costco')
                self.assertEqual(request.status_code, 200)
                # self.assertEqual(StoreModel.find_by_name('costco'))
                self.assertDictEqual({'name': 'costco', 'item': []},
                                     json.loads(request.data))




    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                request = client.get('/store/costco')
                self.assertEqual(request.status_code, 404)
                self.assertDictEqual({'message': 'Store not found'},
                                     json.loads(request.data))

    def test_store_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('costco').save_to_db()
                ItemModel('pc', 1500, 1).save_to_db()
                request = client.get('/store/costco')
                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'message': 'costco', 'item': [{'name': 'pc', 'price': 1500}]},
                                     json.loads(request.data))


    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('costco').save_to_db()
                request = client.get('/stores')
                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'stores': [{'name': 'costco', 'item':[]}]},
                                     json.loads(request.data))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('costco').save_to_db()
                ItemModel('pc', 1500, 1).save_to_db()
                request = client.get('/stores')
                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'stores': [{'name': 'costco', 'item': [{'name': 'pc', 'price': 1500}]}]},
                                     json.loads(request.data))