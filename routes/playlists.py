from flask import Blueprint, request, jsonify
from ytmusicapi import YTMusic

bp = Blueprint('playlists', __name__)
ytmusic = YTMusic()

@bp.route('/api/playlist/<playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    """
    Get detailed information about a playlist including all tracks
    Path params:
        - playlist_id: Playlist ID
    Query params:
        - limit: Number of tracks to return (optional, default: 100)
    """
    try:
        if not playlist_id:
            return jsonify({'error': 'Playlist ID is required'}), 400
        
        limit = int(request.args.get('limit', 100))
        
        # Get playlist details
        playlist_info = ytmusic.get_playlist(playlist_id, limit=limit)
        
        return jsonify({
            'success': True,
            'playlistId': playlist_id,
            'data': playlist_info
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
