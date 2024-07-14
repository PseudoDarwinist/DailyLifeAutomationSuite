# Python script (save as wifi_qr_generator.py)
import qrcode

def generate_wifi_qr(ssid, password, security='WPA'):
    try:
        # Create Wi-Fi network string
        if security.upper() not in ['WPA', 'WEP', '']:
            raise ValueError("Security must be 'WPA', 'WEP', or '' for open networks")

        # Check if password is numeric
        if password.isdigit():
            password = f'"{password}"'  # Wrap numeric password in quotes
        else:
            password = password.replace(';', '\\;').replace(',', '\\,').replace(':', '\\:')

        wifi_string = f"WIFI:T:{security};S:{ssid};P:{password};;"

        # Create QR code instance
        qr = qrcode.QRCode(version=1, box_size=10, border=5)

        # Add data to the QR code
        qr.add_data(wifi_string)
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image
        img.save("wifi_qr_code.png")

        print("Wi-Fi QR code has been generated and saved as 'wifi_qr_code.png'")
        print(f"Wi-Fi string: {wifi_string}")  # For debugging
    except ValueError as e:
        print(f"Error: {e}")
        print("Please check your Wi-Fi details and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Wi-Fi network details
ssid = "JioFiber-304_5G"
password = "11223344"
security = "WPA"  # Can be 'WPA', 'WEP', or '' for open networks

generate_wifi_qr(ssid, password, security)





