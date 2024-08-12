from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        # Save the uploaded file
        video_file = request.files['video']
        if video_file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
            video_file.save(filepath)
            # Process the video using pyscenedetect or similar
            # Redirect to the video breakdown page
            return redirect(url_for('video_breakdown', filename=video_file.filename))
    return render_template('upload.html')

@app.route('/video/<filename>')
def video_breakdown(filename):
    # Logic to display the original and split videos
    return render_template('video_breakdown.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)