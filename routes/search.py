from flask import Blueprint, request, jsonify
from ytmusicapi import YTMusic

bp = Blueprint('search', __name__)
ytmusic = YTMusic()

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
        query = request.args.get('query')
        if not query:
            return jsonify({'error': 'Query parameter is required'}), 400
        
        filter_type = request.args.get('filter', None)
        limit = int(request.args.get('limit', 20))
        
        # Validate filter type
        valid_filters = ['songs', 'albums', 'artists', 'playlists', 'videos', 'featured_playlists', 'community_playlists']
        if filter_type and filter_type not in valid_filters:
            return jsonify({'error': f'Invalid filter. Must be one of: {", ".join(valid_filters)}'}), 400
        
        # Perform search
        results = ytmusic.search(query, filter=filter_type, limit=limit)
        
        return jsonify({
            'success': True,
            'query': query,
            'filter': filter_type,
            'count': len(results),
            'results': results
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
