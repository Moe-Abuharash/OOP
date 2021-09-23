import Exercise2

def main():
    manufact_name = input('What is the manufactuer name?: ')
    model_name = input('What is the model name?: ')
    retail_price = input('Whats the pricetag?: ')

    phone_class = phone.PhoneClass(manu, model, price)

    print('This is out data:')
    print('The Manufactuer is: ', phone_class.return_manufact())
    print('The Model is: ', phone_class.return_model())
    print('The Retail Price is: ', phone_class.return_retail_price())

main()
