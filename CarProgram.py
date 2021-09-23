import Car

def main():

    year_model = input("Enter your car year and model: ")
    make = input('Enter you car make: ')

    car = Car.Cars(year_model, make)
    

    for i in range(1,6):
        car.accelerate()
        print('Car speed before brakes is: ',car.get_speed())


    for x in range(1,6):
        car.brake()
        print('Car speed after brakes is: ',car.get_speed())
    



main()
