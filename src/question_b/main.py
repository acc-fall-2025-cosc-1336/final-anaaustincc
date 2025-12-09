from question_b import Stock


def get_stock_list():
    """Create and return a list with Stock class data"""
    stock_list = [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]
    return stock_list


def display_stock_list(stocks):
    """Display the stock purchase history"""
    print("\n" + "="*50)
    print("Stock Purchase History")
    print("="*50)
    print(f"{'Symbol':<10} {'Company Name':<30}")
    print("-"*50)
    for stock in stocks:
        print(f"{stock.get_symbol():<10} {stock.get_company_name():<30}")
    print("="*50)


def main():
    """Main function with menu loop"""
    # Get the stock list and save to a variable
    stocks = get_stock_list()
    
    # Program continues until user opts out
    while True:
        print("\n" + "="*50)
        print("Stock Menu")
        print("="*50)
        print("1-Display stock purchase history")
        print("2-Exit")
        print("="*50)
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Option 1 calls the stock_list function and displays data
            display_stock_list(stocks)
        elif choice == "2":
            # Option 2 exits the program
            print("Thank you for using the stock program!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


# Run the main function
main()