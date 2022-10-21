#Миксины - класс, который будет использоватся для наследования, от максинов не создаются обьекты

class CreateMixin:
    def product_create(self, title, price):
        #self.__class__ - обращение к классу, который наследовался от этого миксина
        model = self.__class__
        _id = ProductCRUD._id
        self.title = title
        self.price = price
        self.id = _id 
        model.objects[_id] = self
        model._id += 1

        

class ReadMixin:
    def product_detail(self, p_id):
        from pprint import pprint
        model = self.__class__
        obj = self.objects.get(p_id)
        pprint({'id':obj.id, 'title':obj.title, 'price':obj.price})

class UpdateMixin:
    pass

class DeleteMixin:
    def delete_product(self):
        model = self.__class__
        model.objects.pop(self.id)

class ProductCRUD(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    objects = {}
    _id = 1

crud = ProductCRUD()
crud.product_create('obj1', 45)
crud.product_create('obj2', 452)
crud.product_detail(1)