import qrcode

# Step 1: Enter the URL and strip any white spaces
url = input("Enter the URL: ").strip()

# Step 2: Create a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Step 3: Add the URL data to the QR code object
qr.add_data(url)
qr.make(fit=True)

# Step 4: Create an image from the QR code object
img = qr.make_image(fill='black', back_color='white')

# Step 5: Save the QR code image
img.save('qr_code.png')

print("QR Code generated and saved as 'qr_code.png'")