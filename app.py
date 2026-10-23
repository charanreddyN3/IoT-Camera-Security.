from flask import Flask, render_template, Response, request
import sqlite3
from camera_stream import generate_frames

app = Flask(__name__)

@app.route('/')
def home():

    search_date = request.args.get('search_date')

    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()

    if search_date:

        cursor.execute("""
            SELECT id,event,time,image_path
            FROM events
            WHERE time LIKE ?
            ORDER BY id DESC
        """, (search_date + "%",))

    else:

        cursor.execute("""
            SELECT id,event,time,image_path
            FROM events
            ORDER BY id DESC
        """)

    events = cursor.fetchall()

    # Graph statistics
    cursor.execute("""
        SELECT substr(time,1,10), COUNT(*)
        FROM events
        GROUP BY substr(time,1,10)
    """)

    stats = cursor.fetchall()

    conn.close()

    latest_event = events[0] if events else None

    dates = [row[0] for row in stats]
    counts = [row[1] for row in stats]

    return render_template(
        "index.html",
        events=events,
        latest_event=latest_event,
        dates=dates,
        counts=counts,
        search_date=search_date
    )

@app.route('/video_feed')
def video_feed():

    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

if __name__ == '__main__':
    app.run(debug=True)