# Phoney Dictate

A voice recognition "app" which sends your cell phone's voice recognition input to your computer.

## Quick start

1. Install from pip

	$ pip install phoney_dictate

2. Run Phoney Dictate on your computer

	$ python3 -m phoney_dictate

<img width="511" height="482" alt="Main Window" src="https://github.com/user-attachments/assets/e5e606a1-4497-43d1-88ad-8ba312d100a7" />

4. Generate a bar code - click on the "QR Code" button at the bottom left
corner of the window.

<img width="620" height="648" alt="Barcode popup" src="https://github.com/user-attachments/assets/59342bf2-2c91-4cfa-8fa7-8c6622dadc1f" />

5. Scan the code with your phone and open the link in your browser. (You may
have to use a tool like "Binary Eye")

6. In your phone's browser, place the cursor in the text area. Whatever you
type or dictate there will appear on the Phoney Dictate application.

7. In the Phoney Dictate application, click the "Copy" button to copy the contents
shown there to the clipboard.

8. Paste the text anywhere.

Whatever is displayed in the browser on your phone will be sent to your
computer. After you clear the text, and enter new text, only the new text will
be copied over. The old text will be gone.

Ctrl-Q exits the Phoney Dictate application on your computer. The browser component
is just a webpage, so you would close it like you normally would any webpage.

## Troubleshooting

Both your phone and your computer need to be on the same local network. Usually
this is the case if your phone and computer are connected to the same router.

This should also work if your computer is set up as a hot spot, although it
hasn't been tested.

If you have a firewall installed on your computer, (such as UFW), make sure
that port **8585** is open for listening.

On machines with UFW:

```bash
$ sudo ufw allow in from <your subnet> port 8585 comment "Phoney Dictate"
```
Replace <your subnet> with the correct value for your home network. Mine is "192.168.1.0/24". 
You can use the "ip" command to get the correct subnet:

```bash
$ ip addr
[...]
3: wlan0: <BROADCAST,MULTICAST...
    [...]
    inet 192.168.1.180/24 brd ...
```
