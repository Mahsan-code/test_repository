from starter_code.models.item  import ItemModel
from starter_code.models.store import StoreModel
from starter_code.tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):

        with self.app_context():
            StoreModel('costco').save_to_db()
            item = ItemModel('costco', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))


    def test_store_relashionship(self):

        with self.app_context:
            store = StoreModel('costco')
            item = ItemModel('pc', 1500, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'costco')

