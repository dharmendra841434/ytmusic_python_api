from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from ytmusicapi import YTMusic

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure CORS
cors_origins = os.getenv('CORS_ORIGINS', '*')
CORS(app, origins=cors_origins)

# Initialize YTMusic client
ytmusic = YTMusic()

# Import routes
from routes import search, songs, albums, artists, playlists, browse, lyrics

# Register blueprints
app.register_blueprint(search.bp)
app.register_blueprint(songs.bp)
app.register_blueprint(albums.bp)
app.register_blueprint(artists.bp)
app.register_blueprint(playlists.bp)
app.register_blueprint(browse.bp)
app.register_blueprint(lyrics.bp)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'YouTube Music API',
        'version': '1.0.0'
    })

# Root endpoint
@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'message': 'YouTube Music API Backend',
        'version': '1.0.0',
        'endpoints': {
            'health': '/api/health',
            'search': '/api/search?query=<query>&filter=<songs|albums|artists|playlists>',
            'song': '/api/song/<videoId>',
            'stream': '/api/song/<videoId>/stream',
            'album': '/api/album/<browseId>',
            'artist': '/api/artist/<browseId>',
            'playlist': '/api/playlist/<playlistId>',
            'home': '/api/home',
            'charts': '/api/charts',
            'lyrics': '/api/lyrics/<browseId>'
        }
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
