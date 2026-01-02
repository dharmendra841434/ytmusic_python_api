from flask import Blueprint, jsonify, request
from utils.ytmusic_utils import get_ytmusic

bp = Blueprint('artists', __name__)

@bp.route('/api/artist/<browse_id>', methods=['GET'])
def get_artist(browse_id):
    """
    Get detailed information about an artist including songs, albums, and singles
    Path params:
        - browse_id: Artist browse ID
    """
    try:
        if not browse_id:
            return jsonify({'error': 'Browse ID is required'}), 400
        
        # Get artist details
        ytmusic = get_ytmusic()
        artist_info = ytmusic.get_artist(browse_id)
        
        return jsonify({
            'success': True,
            'browseId': browse_id,
            'data': artist_info
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/api/artist/<browse_id>/albums', methods=['GET'])
def get_artist_albums(browse_id):
    """
    Get all albums from an artist
    Path params:
        - browse_id: Artist browse ID
    """
    try:
        if not browse_id:
            return jsonify({'error': 'Browse ID is required'}), 400
        
        # Get artist albums
        ytmusic = get_ytmusic()
        artist_info = ytmusic.get_artist(browse_id)
        albums = artist_info.get('albums', {}).get('results', [])
        
        return jsonify({
            'success': True,
            'browseId': browse_id,
            'albums': albums
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
