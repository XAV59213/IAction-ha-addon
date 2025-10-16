from flask import Flask, Response, render_template
import subprocess
import os
import logging
import urllib.parse

app = Flask(__name__, template_folder="templates")

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Charger les variables d'environnement depuis .env
RTSP_URL = os.getenv("DEFAULT_RTSP_URL", "rtsp://192.168.0.180/live")
RTSP_USERNAME = os.getenv("RTSP_USERNAME", "freeboxcam")
RTSP_PASSWORD = urllib.parse.quote(os.getenv("RTSP_PASSWORD", "RUSA%2BqgD"))

def generate_hls_stream():
    """Génère un flux HLS à partir du flux RTSP."""
    logger.info(f"Starting HLS stream for {RTSP_URL}")
    command = [
        "ffmpeg",
        "-i", f"rtsp://{RTSP_USERNAME}:{RTSP_PASSWORD}@{RTSP_URL.split('://')[1]}",
        "-c:v", "copy",  # Copier le flux vidéo sans ré-encodage
        "-c:a", "aac",   # Encoder l'audio en AAC
        "-f", "hls",     # Format HLS
        "-hls_time", "2",  # Durée des segments HLS (2 secondes)
        "-hls_list_size", "3",  # Nombre de segments dans la playlist
        "-hls_flags", "delete_segments",  # Supprimer les anciens segments
        "-hls_segment_filename", "/tmp/stream_%03d.ts",  # Fichiers temporaires
        "/tmp/stream.m3u8"  # Fichier de playlist HLS
    ]

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Attendre que le fichier playlist soit créé
        while not os.path.exists("/tmp/stream.m3u8"):
            pass

        with open("/tmp/stream.m3u8", "rb") as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                yield data
    except Exception as e:
        logger.error(f"Erreur lors de la génération du flux HLS : {e}")
        yield b"Erreur lors de la génération du flux"

@app.route("/stream")
def stream():
    """Endpoint pour diffuser le flux HLS."""
    return Response(generate_hls_stream(), mimetype="application/vnd.apple.mpegurl")

@app.route("/video")
def video_page():
    """Page web pour afficher le flux vidéo."""
    return render_template("video.html")

@app.route("/admin")
def admin():
    """Page d'administration."""
    return render_template("admin.html")

# Endpoints existants (basés sur les logs)
@app.route("/api/admin/config", methods=["GET"])
def get_config():
    return {"status": "success", "config": {}}, 200

@app.route("/api/admin/reload", methods=["POST"])
def reload_config():
    return {"status": "success"}, 200

@app.route("/api/admin/restart", methods=["POST"])
def restart():
    return {"status": "success"}, 200

@app.route("/api/metrics", methods=["GET"])
def metrics():
    return {"status": "success", "metrics": {}}, 200

@app.route("/api/admin/mqtt_test", methods=["GET"])
def mqtt_test():
    return {"status": "success"}, 200

@app.route("/api/admin/rtsp_test", methods=["POST"])
def rtsp_test():
    return {"status": "success"}, 200

@app.route("/api/admin/ai_test", methods=["GET"])
def ai_test():
    return {"status": "success"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
