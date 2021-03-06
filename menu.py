# import tkinter as tk
#
#
# def btn_click(choice):
#     if choice == 'register':
#         Register()
#     elif choice == 'enter':
#         Enter()
#     elif choice == 'exit':
#         Exit()
#
#
# class Register:
#     def __init__(self):
#         print('registered')
#         window = tk.Tk()
#         frame1 = tk.Frame(master=window, width=400, height=100, bg='blue')
#         frame1.pack()
#         label1 = tk.Label(master=frame1, text="Enter your info", font=('arial', 30), bg="white")
#         label1.place(x=0, y=0)
#
#
# class Enter:
#     def __init__(self):
#         print('entered')
#         window = tk.Tk()
#         frame2 = tk.Frame(master=window, width=400, height=100, bg="green")
#         frame2.pack()
#         label2 = tk.Label(master=frame2, text="Enter your info", font=('arial', 30), bg="white")
#         label2.place(x=0, y=0)
#
#
# class Exit:
#     def __init__(self):
#         print('exited')
#         window = tk.Tk()
#         frame3 = tk.Frame(master=window, width=400, height=100, bg="red")
#         frame3.pack()
#         label3 = tk.Label(master=frame3, text="Exit", font=('arial', 30), bg="white")
#         label3.place(x=0, y=0)
#
#
# cal = tk.Tk()
# cal.title("MENU")
#
# btn_register = tk.Button(cal, padx=160, pady=20, bd=10, fg='blue', font=('arial', 20, 'bold'),
#                          text="Do not have an account?Register", command=lambda: btn_click('register')).grid(row=0,
#                                                                                                              column=0)
# btn_enter = tk.Button(cal, padx=160, pady=20, bd=10, fg='green', font=('arial', 20, 'bold'),
#                       text='Already have an account? Enter', command=lambda: btn_click('enter')).grid(row=1, column=0)
# btn_exit = tk.Button(cal, padx=160, pady=20, bd=10, fg='red', font=('arial', 20, 'bold'),
#                      text='Exit', command=lambda: btn_click('exit')).grid(row=2, column=0)
#
# cal.mainloop()
import sing_in
import logging
from manager import Manager
from customer import Customer


# This function execute in the first of program
def menu():
    logging.basicConfig(filename='records.log', filemode='a', format='%(asctime)s  -  %(levelname)s - %(message)s',
                        level=logging.INFO)
    choice = 0
    while choice != 3:  # get option until quitting the program
        print("1-Don't you have an account? Register.")
        print("2-Already have an account? Enter.")
        print("3-Exit.")
        print()
        try:
            choice = int(input("Please Enter your option:  "))
            if not 1 <= choice <= 3:
                raise Exception("There is not such an option!")
        except Exception as error:
            print(f"{error}, Please Enter number between 1 to 3!")
            logging.error(f"{error}  , Happened in menu.")
        if choice == 1:
            sing_in.register()
        elif choice == 2:
            user = False
            while not user:  # until all things add in the right way
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                user = sing_in.check_enter(username, password)  # check if the entered info are true
                if not user:  # if information was not true
                    logging.warning(f"Someone with username {username} tried to enter but it was not successful.")
            logging.info(f"User {user['username']} entered.")
            if user['role'] == 'manager':
                ob = Manager(user)
                ob.show_managers_access()  # information was true and go to access menu
            elif user['role'] == 'client':
                ob = Customer(user)
                ob.show_customers_access()  # information was true and go to access menu
        elif choice == 3:
            print("Have a great time. Goodbye!")


menu()
