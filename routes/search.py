from flask import Blueprint, request, jsonify
from utils.ytmusic_utils import get_ytmusic

bp = Blueprint('search', __name__)

@bp.route('/api/search', methods=['GET'])
def search():
    """
    Search for songs, albums, artists, or playlists
    Query params:
        - query: Search query string (required)
        - filter: Filter type - songs, albums, artists, playlists, videos (optional)
        - limit: Number of results (default: 20)
    """
    try:
        query = request.args.get('query', '').strip()
        
        # If query is empty, use 'Trending' to return mixed data as requested
        if not query:
            query = "Trending"
        
        filter_type = request.args.get('filter', None)
        limit = int(request.args.get('limit', 20))
        
        # Validate filter type
        valid_filters = ['songs', 'albums', 'artists', 'playlists', 'videos', 'featured_playlists', 'community_playlists']
        if filter_type and filter_type not in valid_filters:
            return jsonify({'error': f'Invalid filter. Must be one of: {", ".join(valid_filters)}'}), 400
        
        # Perform search
        ytmusic = get_ytmusic()
        # ignore_spelling=True handles 'spelling false' requirement
        results = ytmusic.search(query, filter=filter_type, limit=limit, ignore_spelling=True)
        
        return jsonify({
            'success': True,
            'query': query,
            'filter': filter_type,
            'count': len(results),
            'results': results
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
