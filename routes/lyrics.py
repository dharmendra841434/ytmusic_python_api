from flask import Blueprint, jsonify, request
from utils.ytmusic_utils import get_ytmusic

bp = Blueprint('lyrics', __name__)

@bp.route('/api/lyrics/<browse_id>', methods=['GET'])
def get_lyrics(browse_id):
    """
    Get lyrics for a song
    Path params:
        - browse_id: Lyrics browse ID (obtained from song details)
    """
    try:
        if not browse_id:
            return jsonify({'error': 'Browse ID is required'}), 400
        
        # Get lyrics
        ytmusic = get_ytmusic()
        lyrics_data = ytmusic.get_lyrics(browse_id)
        
        return jsonify({
            'success': True,
            'browseId': browse_id,
            'data': lyrics_data
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
