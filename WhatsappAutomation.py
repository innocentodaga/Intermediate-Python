import pyautogui
import time
import pyperclip  # For copying and pasting the message from clipboard

def send_messages(file_path, message):
    # Read phone numbers from the file
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()

    for number in numbers:
        try:
            # Search for the contact
            pyautogui.hotkey('ctrl', 'f')  # Open search in WhatsApp
            time.sleep(1)
            pyautogui.write(number)  # Type the phone number or name of the contact
            time.sleep(2)  # Give it time to search
            pyautogui.press('enter')  # Press Enter to select the contact

            # Paste and send the message
            pyperclip.copy(message)  # Copy the message to clipboard
            pyautogui.hotkey('ctrl', 'v')  # Paste the message from clipboard
            time.sleep(1)
            pyautogui.press('enter')  # Send the message
            print(f"Message sent to {number}")

            # Wait for 5 seconds before sending the next message
            time.sleep(5)

        except Exception as e:
            print(f"Failed to send message to {number}. Error: {str(e)}")

# Usage
file_path = "numbers.txt"  # Path to your text file with numbers
message = """Hello, 🤩 👋 
I'm .Dev. io - a curious soul with a passion for machine learning and creative solutions. Connect with me for:

- Meaningful friendships and fun conversations🥰
- Exclusive industry insights and trends📊📈
- Collaborative opportunities and networking🤝
- Expert advice on related projects😁
- Exploring new ideas and innovative thinking🪄
- Page follows 🤗
- Status updates🫠
- Fun facts, memes, and humor to brighten your day🥳
- Potential partnerships and collaborations🤝🫂

Let's connect, share ideas, and create something amazing together! 
Save my contact and let's stay in touch! Reply with your name for a save back 🥰"""

send_messages(file_path, message)
