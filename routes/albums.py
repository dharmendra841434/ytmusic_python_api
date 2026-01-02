from flask import Blueprint, jsonify, request
from utils.ytmusic_utils import get_ytmusic

bp = Blueprint('albums', __name__)

@bp.route('/api/album/<browse_id>', methods=['GET'])
def get_album(browse_id):
    """
    Get detailed information about an album including all tracks
    Path params:
        - browse_id: Album browse ID
    """
    try:
        if not browse_id:
            return jsonify({'error': 'Browse ID is required'}), 400
        
        # Get album details
        ytmusic = get_ytmusic()
        album_info = ytmusic.get_album(browse_id)
        
        return jsonify({
            'success': True,
            'browseId': browse_id,
            'data': album_info
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
