from mycroft import MycroftSkill, intent_file_handler


class PizzaOrder(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('order.pizza.intent')
    def handle_order_pizza(self, message):
        self.speak_dialog('order.pizza')


def create_skill():
    return PizzaOrder()

