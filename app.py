from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import torch
from ultralytics import YOLO
import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)
model = YOLO('/Users/mariaelenagarciabaiz/Desktop/Captone/best.pt')  # Adjust the path to your model

actual_recipe = ['banana']  # Replace with actual ingredients

def send_email_alert(to_email, subject, message):
    from_email = 'mariaelena.garcia@utp.edu.co'  # Replace with your email
    from_password = 'vjjb odjf ryrw ltyq'  # Replace with your app-specific password

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_predictions_and_send_alert(predictions):
    detected_classes = [prediction['class'] for prediction in predictions]
    send_alert = False

    for pred in detected_classes:
        if pred not in actual_recipe:
            send_alert = True
            break
    for act in actual_recipe:
        if act not in detected_classes:
            send_alert = True
            break

    if send_alert:
        message = 'Incorrect or missing ingredient detected.'
        send_email_alert('mariaelena.garcia@utp.edu.co', 'Ingredient Alert', message)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    img_bytes = file.read()
    img = Image.open(io.BytesIO(img_bytes))

    results = model(img)
    predictions = []
    for result in results[0].boxes.data.tolist():
        bbox = result[:4]
        class_id = int(result[-1])
        score = result[4]
        predictions.append({
            'bbox': bbox,
            'class': model.names[class_id],
            'score': score
        })

    # Ensure evaluation logic is called here
    check_predictions_and_send_alert(predictions)
    
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True, port=5001)