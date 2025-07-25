import qrcode
import random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)

def nomes_images(tam):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(tam))
    return result_str

@app.route('/url', methods=['POST'])
def get_url_qrcode():
    url_data = request.json['url']
    qr = qrcode.QRCode(version=1, box_size=10, border=2)

    qr.add_data(url_data)

    qr.make(fit=True)
    
    image = qr.make_image(fill_color='black', back_color='white')

    name_image = nomes_images(15) + '.png'

    image.save(name_image)

    return jsonify(image_name = name_image)
    

if __name__ == '__main__':
    app.run()