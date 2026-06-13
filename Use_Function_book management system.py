from menu import print_main
from heading import heading
from messaage import closing_msg, Last_msg

# create new book
books = []


while True:
    print_main()
    user_input = int(input("Enter your choice: "))

    if user_input == 0:
        closing_msg()
        break

    
    if user_input == 0:
        Last_msg()
        break

    # Create new book
    if user_input == 1:
        heading("Create new book")

        book_name = input("Enter Book Name: ")
        book_qty = int(input("Enter Initial Book Quantity: "))

        new_book = {
            "name": book_name,
            "qty": book_qty
        }
        books.append(new_book)

        print(f"Book Name: {book_name} Successfully Added")
        Last_msg()

        user_input_add = int(input("Enter your choice: "))
        if user_input_add == 0:
            closing_msg()
            break

    # List of books
    if user_input == 2:
        heading("List of books")

        print(f"{'-'*45}")
        print(f"|{'Book Name':^20} | {'Quantity':^20}|")
        print(f"{'-'*45}")

        for book in books:
            print(f"|{book['name']:^20} | {book['qty']:^20}|")
            print(f"{'-'*45}")

        Last_msg()

        user_input_add = int(input("Enter your choice: "))
        if user_input_add == 0:
            closing_msg()
            break

    # Sell a book
    if user_input == 3:
        found = False
        heading("Sell a Book")

        search_book_name = input("Enter Book Name: ")

        for book in books:
            if search_book_name == book["name"]:
                found = True
                print("The requested book Found!")

                sell_qty = int(input("Enter Sell Quantity: "))
                inventory_qty = book["qty"]

                if sell_qty <= inventory_qty:
                    book["qty"] = inventory_qty - sell_qty
                else:
                    print("Not enough stock!")

                break

        if found == False:
            print("The requested book was not found")

        Last_msg()

        user_input_sell = int(input("Enter your choice: "))
        if user_input_sell == 0:
            closing_msg()
            break

    # Update book quantity
    if user_input == 4:
        found = False
        heading("Update book quantity")

        search_book_name = input("Enter Book Name: ")

        for book in books:
            if search_book_name == book["name"]:
                found = True
                print("The requested book Found!")

                update_qty = int(input("Enter update Quantity: "))
                inventory_qty = book["qty"]

                if update_qty > 0:
                    book["qty"] = inventory_qty + update_qty
                    print(f"Book quantity updated! New quantity: {book['qty']}")
                else:
                    print("Update quantity must be greater than 0")

                break

        if found == False:
            print("The requested book was not found")

        Last_msg()

        user_input_sell = int(input("Enter your choice: "))
        if user_input_sell == 0:
            closing_msg()
            break

    # Delete a book

    if user_input == 5:
        found = False
        heading("Delete a Book")

        search_book_name = input("Enter Book Name: ")

        for book in books:
            if search_book_name == book["name"]:
                found = True
                print("The requested book Found!")

                confirm = input(f"Are you sure you want to delete '{book['name']}'? (yes/no): ")

                if confirm.lower() == "yes":
                    books.remove(book)
                    print(f"Book '{search_book_name}' has been deleted successfully!")
                else:
                    print("Deletion cancelled!")
                break
            
        if found == False:
            print("The requested book was not found")

        Last_msg()

        user_input_sell = int(input("Enter your choice: "))
        if user_input_sell == 0:
            closing_msg()
            break

    # Ghost book

    if user_input == 6:
        heading("Ghost book")
        ghost_book_name = input("Enter Ghost book name: ")
        ghost_book_qty = int(input("Enter ghost book quantity: "))
        ghost_book = {
            "name": ghost_book_name,
            "qty": ghost_book_qty
        }
        books.append(ghost_book)
        print(f"ghost book '{ghost_book_name}' added successfully!")
        Last_msg()
