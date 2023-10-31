import flask
import cv2
from flask import Flask, request, url_for, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

def gen_camera_feed_sales():
    cap0 = cv2.VideoCapture('rtsp://admin:ccs@1234@192.168.100.119:554/cam/realmonitor?channel=1&subtype=0')
    
    while True:
        success, frame = cap0.read()
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            break
        frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        


def gen_camera_feed_ai():
    cap1 = cv2.VideoCapture('rtsp://admin:ccs@1234@192.168.100.114:8554/cam/realmonitor?channel=1&subtype=0')
    
    while True:
        success, frame = cap1.read()
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            break
        frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
    
def gen_camera_feed_presales():
    cap2 = cv2.VideoCapture('rtsp://admin:ccs@1234@192.168.100.115:554/cam/realmonitor?channel=1&subtype=0')
    
    while True:
        success, frame = cap2.read()
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            break
        frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/button_action', methods=['POST'])
# def button_action():
#     button = request.form['button']

#     cap0 = cv2.VideoCapture('rtsp://admin:ccs@1234@192.168.100.115:554/cam/realmonitor?channel=1&subtype=0')
#     cap1 = cv2.VideoCapture('rtsp://admin:ccs@1234@192.168.100.114:554/cam/realmonitor?channel=1&subtype=0')
#     cap2 = cv2.VideoCapture('rtsp://admin:ccs@1234@192.168.100.119:554/cam/realmonitor?channel=1&subtype=0')

    # if button == "Sales":
    #     gen_camera_feed_sales()
    #     return Response(gen_camera_feed_sales(), mimetype='multipart/x-mixed-replace; boundary=frame')
    #     #while True:
    #         #success, frame = cap0.read()
    #         #if not success:
    #             #break
    #         #ret, buffer = cv2.imencode('.jpg', frame)
    #         #if not ret:
    #             #break
    #         #frame = buffer.tobytes()
    #         #yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # elif button == "AI":
    #     return Response(gen_camera_feed_ai(), mimetype='multipart/x-mixed-replace; boundary=frame')

    # elif button == "Presales":
    #     return Response(gen_camera_feed_presales(), mimetype='multipart/x-mixed-replace; boundary=frame')

    # #return Response(gen_camera_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed')
def video_feed():
    return Response(gen_camera_feed_presales(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/ai', methods = ['POST'])
def ai():
    button = request.form.get('button')
    if button == "AI":
        return render_template('ai.html')
    
@app.route('/sales', methods = ['POST'])
def sales():
    button = request.form.get('button')
    if button == "Sales":
        return render_template('sales.html')
    
@app.route('/presales', methods = ['POST'])
def presales():
    button = request.form.get('button')
    if button == "Presales":
        return render_template('presales.html')
    
@app.route('/ai_vid')
def ai_vid():
    return Response(gen_camera_feed_ai(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/sales_vid')
def sales_vid():
    return Response(gen_camera_feed_sales(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/presales_vid')
def presales_vid():
    return Response(gen_camera_feed_presales(), mimetype='multipart/x-mixed-replace; boundary=frame')

        
    


# def button_click():
#     button = request.form.get('button') 
#     if button == "Sales":
#         #return Response(gen_camera_feed_sales(), mimetype='multipart/x-mixed-replace; boundary=frame')
#         return render_template("sales.html")
    
#     elif button == "AI":
#         return Response(gen_camera_feed_ai(), mimetype='multipart/x-mixed-replace; boundary=frame')
        
    
#     elif button == "PreSales":
#         return Response(gen_camera_feed_presales(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
    
           
if __name__ == "__main__":
    app.run(debug = True)

#Button click for a particular team