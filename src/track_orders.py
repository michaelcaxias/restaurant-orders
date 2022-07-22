class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        dish_customer = {}

        for name, order, _day in self.orders:
            if name == customer:
                if order not in dish_customer:
                    dish_customer[order] = 1
                else:
                    dish_customer[order] += 1

        return max(dish_customer, key=dish_customer.get)

    def get_never_ordered_per_customer(self, customer):
        plates = set()
        customer_plates = set()
        for name, order, _day in self.orders:
            plates.add(order)
            if name == customer:
                customer_plates.add(order)

        return plates.difference(customer_plates)

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
