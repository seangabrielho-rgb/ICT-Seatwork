
from js import document
from pyodide.ffi import create_proxy
club_members = [
    "John Wick",
    "Saint Nicolas",
    "Logan Paul",
    "Bomb Squad 14",
    "Coco Martin"
]
def check_membership(event):
    first_name = document.getElementById("fname").value.strip()
    last_name = document.getElementById("lname").value.strip()
    full_name = f"{first_name} {last_name}".strip()
    full_name_lower = full_name.lower()
    members_lower = list(map(str.lower, club_members))
    is_member = full_name_lower in members_lower
    messages = [
        f"Sorry not sorry {full_name}, your name is not on the list, get out.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    ]
    document.getElementById("result").innerText = messages[is_member]
def setup(event=None):
    document.getElementById("members-list").innerText = ", ".join(club_members)
    button = document.getElementById("btn-submit")
    button.addEventListener("click", create_proxy(check_membership))
setup()