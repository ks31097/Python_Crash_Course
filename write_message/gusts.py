import time
from datetime import datetime, timedelta

def added_time():
    # Get the current time in readable format
    current_time = time.time()
    readable_time = datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')
    return readable_time

def guest_name():
    name = input("What is your name?\t")
    return name

def create_list(filename):
    try:
        while True:
            with open(filename, 'a') as file_object:
                name = str(guest_name()).strip().capitalize()
                # breakpoint()
                if name.lower() == 'exit()' or name.lower() == 'exit':

                    # message = f"""
                    # The entered information is saved in a file.
                    # You can file file at: {filename}
                    # """
                    # print(message)
                    
                    print("The entered information is saved in a file.")
                    print(f"You can file file at: {filename}")
                    break
            
                file_object.write(f"{name} was added into the list at:{added_time()}\n")
                print(f"Guest {name} in the list.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
        filename = 'write_message/guests_list.txt'
        create_list(filename)
