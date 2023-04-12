contact={}

def displaycontact():
    print("Name\t\tContact No.")
    for name in contact:
        print("{}\t\t{}".format(name,contact.get(name)))


while True:
    options=int(input(" 1. Add new contact \n 2. Search a contact \n 3. Display \n 4. Edit \n 5. Delete \n 6. Exit \n Enter Your Choice:"))
    if options == 1:
        name=input("Enter the name:")
        contact_no=input("Enter the number:")
        contact[name]=contact_no
    elif options == 2:
        search_name=input("Enter the name to search:")
        if search_name in contact:
            print(search_name,"'s contact no. is:",contact[search_name])
        else:
            print("Not Found")
    elif options == 3:
        if not contact:
            print("Empty")
        else:
            displaycontact()
    elif options == 4:
        edit=input("Enter the contact name to edit:")
        if edit in contact:
            edited_contact=input("Enter the new number:")
            contact[edit]=edited_contact
            print("Updated")
            displaycontact()
        else:
            print("Not Found")
    elif options == 5:
        deletion=input("Enter the contact name to delete:")
        if deletion in contact:
            delete=input("Confirm with Y/N to delete the number:")
            if delete=="Y" or delete=="y":
                contact.pop(deletion)
            else:
                displaycontact()
        else:
            print("Not Found")

    else:
        break



