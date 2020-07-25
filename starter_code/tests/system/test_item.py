from starter_code.models.item import ItemModel
from starter_code.models.store import StoreModel
from starter_code.models.user import UserModel
from starter_code.tests.base_test import BaseTest
import  json

class ItemTest(BaseTest):

    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():

                request = client.get('/item/pc')
                self.assertEqual(request.status_code, 401)


    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                UserModel('mahsan', '1234mah').save_to_db()
                auth_respond = client.post('/auth',
                                           data=json.dumps({'username': 'mahsan', 'password': 'mah1234'}),
                                           header={'content_type': 'application/json'})
                auth_token = json.loads(auth_respond.data)['access_token']
                header = {'authorization': f'JWT {auth_token}'}

                resp = client.get('/item/pc', header = header)
                self.assertEqual(resp.status_code, 404)


    def test_get_item(self):
        pass

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('costco').save_to_db()
                ItemModel('pc', 1500).save_to_db()
                request = client.delete('/item/pc')
                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'message': 'Item deleted'},
                                     json.loads(request.data))

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('costco').save_to_db()

                request = client.post('/item/pc', data={'price': 1500, 'store_id': 1})
                self.assertEqual(request.status_code, 200)

                self.assertDictEqual({'name': 'pc', 'price': 1500},
                                     json.loads(request.data))
    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('costco').save_to_db()
                ItemModel('pc', 1500,1).save_to_db()
                request = client.post('/item/pc', data= {'name': 'pc', 'store_id': 1})
                self.assertEqual(request.status_code, 400)
                self.assertDictEqual({'message': 'n item with name pc already exists.'},
                                     json.loads(request.data))

    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('costco').save_to_db()

                request = client.put('/item/pc', data={'name': 'pc', 'store_id': 1})
                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'name': 'pc','price': 1500},
                                     json.loads(request.data))

    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('costco').save_to_db()
                ItemModel('pc', 1450, 1)
                request = client.get('/item/pc')

                self.assertDictEqual({'item':[{'name': 'pc', 'price': 1500}]},
                                     json.loads(request.data))








    def test_item_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('costco').save_to_db()
                ItemModel('pc', 1450, 1)
                request = client.put('/item/pc', data={'price': 1500, 'store_id': 1})
                self.assertEqual(request.status_code, 200)
                self.assertDictEqual({'name': 'pc', 'price': 1500},
                                     json.loads(request.data))



