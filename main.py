import webbrowser
import requests
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import filedialog

def menu():
    # Fenster erstellen und Größe anpassen
    window = Tk()
    window.geometry("400x490")
    window.title("Webhook message builder V1.0.0 ©")

    # Hintergrundfarbe
    window.configure(bg='#5865F2')

    # Textfeld für die Webhook-URL
    webhook_label = Label(window, text="𝐖𝐞𝐛𝐡𝐨𝐨𝐤 𝐔𝐑𝐋:", font=("Arial Bold", 14), bg='#5865F2', fg='white')
    webhook_label.pack()
    webhook_entry = Entry(window, width=50)
    webhook_entry.pack()

    # Nachrichteninhalt
    message_label = Label(window, text="𝐓𝐞𝐱𝐭 (𝐰𝐢𝐭𝐡𝐨𝐮𝐭 𝐞𝐦𝐛𝐞𝐝):", font=("Arial Bold", 14), bg='#5865F2', fg='white')
    message_label.pack()
    message_entry = Entry(window, width=50)
    message_entry.pack()

    # Absendername
    sender_label = Label(window, text="𝐍𝐚𝐦𝐞:", font=("Arial Bold", 14), bg='#5865F2', fg='white')
    sender_label.pack()
    sender_entry = Entry(window, width=50)
    sender_entry.pack()

    # Embed Aufbau
    embed_label = Label(window, text="𝐁𝐮𝐢𝐥𝐝 𝐞𝐦𝐛𝐞𝐝:", font=("Arial Bold", 14), bg='#5865F2', fg='white')
    embed_label.pack()

    # Embed-Titel
    embed_title_label = Label(window, text="𝐂𝐨𝐧𝐭𝐞𝐧𝐭:", font=("Arial Bold", 12), bg='#5865F2', fg='white')
    embed_title_label.pack()
    embed_title_entry = Entry(window, width=50)
    embed_title_entry.pack()

    # Embed-Beschreibung
    embed_desc_label = Label(window, text="𝐄𝐦𝐛𝐞𝐝 𝐓𝐞𝐱𝐭:", font=("Arial Bold", 12), bg='#5865F2', fg='white')
    embed_desc_label.pack()
    embed_desc_entry = Entry(window, width=50)
    embed_desc_entry.pack()

    # Embed-Farbe
    def choose_color():
        color = colorchooser.askcolor()[1]
        embed_color_entry.delete(0, END)
        embed_color_entry.insert(0, color)

    embed_color_label = Label(window, text="𝐜𝐨𝐥𝐨𝐫:", font=("Arial Bold", 12), bg='#5865F2', fg='white')
    embed_color_label.pack()
    embed_color_entry = Entry(window, width=50)
    embed_color_entry.pack()
    embed_color_button = Button(window, text="𝐂𝐡𝐨𝐨𝐬𝐞 𝐜𝐨𝐥𝐨𝐫", command=choose_color)
    embed_color_button.pack()



        # Schaltfläche zum Senden der Nachricht
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

        # JSON-Payload für die eingebettete Nachricht erstellen
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

        # Antwort des Servers prüfen
        if response.status_code == 204:
            messagebox.showinfo("success", " 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐬𝐞𝐧𝐭 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲!")
        else:
            messagebox.showerror("𝐄𝐫𝐫𝐨𝐫", f"𝐄𝐫𝐫𝐨𝐫 {response.status_code}: 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐜𝐨𝐮𝐥𝐝 𝐧𝐨𝐭 𝐛𝐞 𝐬𝐞𝐧𝐭.")

                    
    send_button = Button(window, text="𝐒𝐞𝐧𝐝 𝐌𝐞𝐬𝐬𝐚𝐠𝐞", command=send_message, bg='#1c1f22', fg='white', padx=10, pady=5)
    send_button.pack()


    def open_discord():
            webbrowser.open("https://solo.to/mrak")
    discord_button = Button(window, text="𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞", command=open_discord, bg='#1c1f22', fg='white', padx=90, pady=5, )
    discord_button.pack(side=BOTTOM, padx=50, pady=50)

    


        # Fenster anzeigen
    window.mainloop()
  
    
if __name__ == "__main__":
     menu()