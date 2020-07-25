from starter_code.models.item import ItemModel
from starter_code.models.store import StoreModel
from unittest import  TestCase


class StoreTest(TestCase):

    def test_create_store(self):

        store = StoreModel('costco')

        self.assertEqual(store.name, 'costco')

    def test_create_store_items_empty(self):

        store = StoreModel('costco')

        self.assertListEqual(store.name.all(), [])


    def test_crud(self):



        with self.app_contex():
            store = StoreModel('costco')
            self.assertIsNone(StoreModel.find_by_name('costco'))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test'))

            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name('costco'))

    def test_relationship_items(self):
        with self.app_contex():
            store = StoreModel('costco')
            item = ItemModel('pc', 1500, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'pc')



    def test_jason(self):
        store = StoreModel('costco')
        item = ItemModel('pc', 1500, 1)


        expected = []

        self.assertEqual(store.json(), expected)

    def test_jason(self):
        store = StoreModel('costco')
        item = ItemModel('pc', 1500, 1)

        store.save_to_db()
        item.save_to_db()

        expected = {'name': 'costco',
                    'items': [{'name': 'pc', 'price': 1500}]}

        self.assertEqual(store.json(), expected)



