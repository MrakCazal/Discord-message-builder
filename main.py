import webbrowser
import requests
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import filedialog

def menu():
    # Fenster erstellen und Grรถรe anpassen
    window = Tk()
    window.geometry("400x490")
    window.title("Webhook message builder V1.0.0 ยฉ")

    # Hintergrundfarbe
    window.configure(bg='#5865F2')

    # Textfeld fรผr die Webhook-URL
    webhook_label = Label(window, text="๐๐๐๐ก๐จ๐จ๐ค ๐๐๐:", font=("Arial Bold", 14), bg='#5865F2', fg='white')
    webhook_label.pack()
    webhook_entry = Entry(window, width=50)
    webhook_entry.pack()

    # Nachrichteninhalt
    message_label = Label(window, text="๐๐๐ฑ๐ญ (๐ฐ๐ข๐ญ๐ก๐จ๐ฎ๐ญ ๐๐ฆ๐๐๐):", font=("Arial Bold", 14), bg='#5865F2', fg='white')
    message_label.pack()
    message_entry = Entry(window, width=50)
    message_entry.pack()

    # Absendername
    sender_label = Label(window, text="๐๐๐ฆ๐:", font=("Arial Bold", 14), bg='#5865F2', fg='white')
    sender_label.pack()
    sender_entry = Entry(window, width=50)
    sender_entry.pack()

    # Embed Aufbau
    embed_label = Label(window, text="๐๐ฎ๐ข๐ฅ๐ ๐๐ฆ๐๐๐:", font=("Arial Bold", 14), bg='#5865F2', fg='white')
    embed_label.pack()

    # Embed-Titel
    embed_title_label = Label(window, text="๐๐จ๐ง๐ญ๐๐ง๐ญ:", font=("Arial Bold", 12), bg='#5865F2', fg='white')
    embed_title_label.pack()
    embed_title_entry = Entry(window, width=50)
    embed_title_entry.pack()

    # Embed-Beschreibung
    embed_desc_label = Label(window, text="๐๐ฆ๐๐๐ ๐๐๐ฑ๐ญ:", font=("Arial Bold", 12), bg='#5865F2', fg='white')
    embed_desc_label.pack()
    embed_desc_entry = Entry(window, width=50)
    embed_desc_entry.pack()

    # Embed-Farbe
    def choose_color():
        color = colorchooser.askcolor()[1]
        embed_color_entry.delete(0, END)
        embed_color_entry.insert(0, color)

    embed_color_label = Label(window, text="๐๐จ๐ฅ๐จ๐ซ:", font=("Arial Bold", 12), bg='#5865F2', fg='white')
    embed_color_label.pack()
    embed_color_entry = Entry(window, width=50)
    embed_color_entry.pack()
    embed_color_button = Button(window, text="๐๐ก๐จ๐จ๐ฌ๐ ๐๐จ๐ฅ๐จ๐ซ", command=choose_color)
    embed_color_button.pack()



        # Schaltflรคche zum Senden der Nachricht
    def send_message():
        # Nachrichteninhalt aus dem Textfeld abrufen
        message = message_entry.get()

        # Webhook-URL aus dem Textfeld abrufen
        webhook_url = webhook_entry.get()

        # Eingebettete Nachricht erstellen
        embed_title = embed_title_entry.get()
        embed_desc = embed_desc_entry.get()
        embed_color = int(embed_color_entry.get()[1:], 16)

         # Absendername aus dem Textfeld abrufen    
        username = sender_entry.get()

        # JSON-Payload fรผr die eingebettete Nachricht erstellen
        payload = {
            "username": username,
            "embeds": [{
                "title": embed_title,
                "description": embed_desc,
                "color": embed_color,
                
                
            }],

            "content": message
        }

        # Nachricht an den Webhook senden
        response = requests.post(webhook_url, json=payload)

        # Antwort des Servers prรผfen
        if response.status_code == 204:
            messagebox.showinfo("success", " ๐๐๐ฌ๐ฌ๐๐?๐ ๐ฌ๐๐ง๐ญ ๐ฌ๐ฎ๐๐๐๐ฌ๐ฌ๐๐ฎ๐ฅ๐ฅ๐ฒ!")
        else:
            messagebox.showerror("๐๐ซ๐ซ๐จ๐ซ", f"๐๐ซ๐ซ๐จ๐ซ {response.status_code}: ๐๐๐ฌ๐ฌ๐๐?๐ ๐๐จ๐ฎ๐ฅ๐ ๐ง๐จ๐ญ ๐๐ ๐ฌ๐๐ง๐ญ.")

                    
    send_button = Button(window, text="๐๐๐ง๐ ๐๐๐ฌ๐ฌ๐๐?๐", command=send_message, bg='#1c1f22', fg='white', padx=10, pady=5)
    send_button.pack()


    def open_discord():
            webbrowser.open("https://solo.to/mrak")
    discord_button = Button(window, text="๐๐จ๐ง๐ญ๐๐๐ญ ๐๐", command=open_discord, bg='#1c1f22', fg='white', padx=90, pady=5, )
    discord_button.pack(side=BOTTOM, padx=50, pady=50)

    


        # Fenster anzeigen
    window.mainloop()
  
    
if __name__ == "__main__":
     menu()