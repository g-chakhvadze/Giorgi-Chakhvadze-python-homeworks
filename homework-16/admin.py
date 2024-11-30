import random

from common import process_user_input
from db import sessions


def list_admin_menu_items():
    print("1. list all sessions ")
    print("2. remove session")
    print("3. add session")
    print("4. edit session")
    return process_user_input()

def greetings():
    print("Welcome to the admin panel")
    print("Please sign in to continue")

def add_session():
    print("Adding session")
    print("Enter the session details")
    film_name = input("Film name: ")
    start_time = input("Start time: ")
    room_number = input("Room number: ")
    room_length = int(input("Room length: "))
    room_width = int(input("Room width: "))
    capacity = room_length * room_width
    # TODO: session_id may be used already, need to check
    session_id = random.randint(1, 1000)
    session = {
        "session_id": session_id,
        "film_name": film_name,
        "start_time": start_time,
        "room_number": room_number,
        "room_length": room_length,
        "room_width": room_width,
        "capacity": capacity
    }
    print("Session added successfully")
    sessions.append(session)
    print("Session added successfully.")


def list_sessions():
    print("Listing sessions")
    if not sessions:
        print("No sessions found")
        return
    for session in sessions:
        print(f"\tSession ID: {session['session_id']}")
        print(f"\tFilm name: {session['film_name']}")
        print(f"\tStart time: {session['start_time']}")
        print(f"\tRoom number: {session['room_number']}")
        print(f"\tRoom length: {session['room_length']}")
        print(f"\tRoom width: {session['room_width']}")
        print(f"\tCapacity: {session['capacity']}")
        print("\n")

def remove_session():
    session_id=int(input("Enter the session ID to remove: "))
    for session in sessions:
        if session['session_id']==session_id:
            sessions.remove(session)
            print("Session removed successfully.")
            return
    print("Session not found.")

def edit_session():
    session_id=int(input("Enter the session id to edit: "))
    for session in sessions:
        if session['session_id'] == session_id:
            print("Editing session details (leave blank to keep current value):")
            session['film_name'] = input(f"Film name ({session['film_name']}): ") or session['film_name']
            session['start_time'] = input(f"Start time ({session['start_time']}): ") or session['start_time']
            session['room_number'] = input(f"Room number ({session['room_number']}): ") or session['room_number']
            session['room_length'] = int(input(f"Room length ({session['room_length']}): ") or session['room_length'])
            session['room_width'] = int(input(f"Room width ({session['room_width']}): ") or session['room_width'])
            session['capacity'] = session['room_length'] * session['room_width']
            print("Session edited successfully")
            return
    print("Session not found.")
def admin_loop():
    greetings()
    while True:
        user_input = list_admin_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":
                remove_session()
            case "3":
                add_session()
            case "4":
                edit_session()
            case _:
                print("Invalid input")

