class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)


from unittest import TestCase, main


class CarTest(TestCase):
    def test_is_car_is_initialized_correctly(self):
        car = Car('Honda', 'Accord', 12, 45)
        self.assertEqual('Honda', car.make)
        self.assertEqual('Accord', car.model)
        self.assertEqual(12, car.fuel_consumption)
        self.assertEqual(45, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_if_make_attribute_is_zero_raise(self):
        with self.assertRaises(Exception) as ex:
            car = Car(0, 'Accord', 12, 45)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_if_make_attribute_is_empty_string_raise(self):
        with self.assertRaises(Exception) as ex:
            car = Car('', 'Accord', 12, 45)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_if_make_attribute_is_None_raise(self):
        with self.assertRaises(Exception) as ex:
            car = Car(None, 'Accord', 12, 45)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_if_model_attribute_is_zero_raise(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Honda', 0, 12, 45)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_if_model_attribute_is_empty_string_raise(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Honda', '', 12, 45)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_if_model_attribute_is_None_raise(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Honda', None, 12, 45)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_is_zero_raise(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Honda', 'Accord', 0, 45)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_is_negative_raise(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Honda', 'Accord', -5, 45)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_is_zero_raise(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Honda', 'Accord', 12, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_is_negative_raise(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Honda', 'Accord', 12, -40)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_is_negative_raise(self):
        car = Car('Honda', 'Accord', 12, 45)
        self.assertEqual(0, car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -5
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_function_receive_zero_fuel_raise(self):
        car = Car('Honda', 'Accord', 12, 45)
        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_function_receive_negative_amount_of_fuel_raise(self):
        car = Car('Honda', 'Accord', 12, 45)
        with self.assertRaises(Exception) as ex:
            car.refuel(-5)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_the_car_with_fuel(self):
        car = Car('Honda', 'Accord', 12, 45)
        self.assertEqual(0, car.fuel_amount)
        car.refuel(30)
        self.assertEqual(30, car.fuel_amount)
        car.refuel(12)
        self.assertEqual(42, car.fuel_amount)

    def test_refuel_the_car_with_more_fuel_than_capacity(self):
        car = Car('Honda', 'Accord', 12, 45)
        self.assertEqual(0, car.fuel_amount)
        car.refuel(47)
        self.assertEqual(45, car.fuel_amount)

    def test_drive_car_given_distance(self):
        car = Car('Honda', 'Accord', 12, 45)
        self.assertEqual(0, car.fuel_amount)
        car.refuel(20)
        self.assertEqual(20, car.fuel_amount)
        car.drive(10)
        self.assertEqual(18.8, car.fuel_amount)

    def test_drive_car_not_enough_fuel_raise(self):
        car = Car('Honda', 'Accord', 12, 45)
        self.assertEqual(0, car.fuel_amount)
        car.refuel(1)
        with self.assertRaises(Exception) as ex:
            car.drive(50)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()