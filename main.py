# Import necessary libraries
from tkinter import *
import requests

# Function to fetch a quote from the API
def fetch_quote():
    # Send a GET request to the API
    request = requests.get(url="https://api.kanye.rest")
    if request.status_code == 200:
        # If the request is successful, parse the JSON response and return the quote
        data = request.json()
        return data["quote"]
    else:
        # If there's an error accessing the API, raise an exception
        raise Exception("Error accessing the API")

# Function to update the displayed quote on the canvas
def get_quote():
    # Call the fetch_quote function to get a new quote
    quote = fetch_quote()
    # Update the text of the quote_text canvas item with the new quote
    canvas.itemconfig(quote_text, text=quote)

# Create the main window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Create a canvas for background
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
canvas.grid(row=0, column=0)

# Create a canvas text item to display the quote
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 20, "bold"), fill="black")

# Create a button with Kanye's image to get a new quote
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Display an initial quote
initial_quote = fetch_quote()
canvas.itemconfig(quote_text, text=initial_quote)

# Start the Tkinter main loop
window.mainloop()
