from flask import Blueprint, jsonify
from ytmusicapi import YTMusic

bp = Blueprint('browse', __name__)
ytmusic = YTMusic()

@bp.route('/api/home', methods=['GET'])
def get_home():
    """
    Get home feed with recommendations and trending content
    """
    try:
        # Get home feed
        home_feed = ytmusic.get_home()
        
        return jsonify({
            'success': True,
            'data': home_feed
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/api/charts', methods=['GET'])
def get_charts():
    """
    Get music charts (top songs, trending, etc.)
    """
    try:
        # Get charts - default country
        charts = ytmusic.get_charts()
        
        return jsonify({
            'success': True,
            'data': charts
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/api/charts/<country>', methods=['GET'])
def get_charts_by_country(country):
    """
    Get music charts for a specific country
    Path params:
        - country: Two-letter country code (e.g., US, GB, IN)
    """
    try:
        if not country:
            return jsonify({'error': 'Country code is required'}), 400
        
        # Get charts for specific country
        charts = ytmusic.get_charts(country=country.upper())
        
        return jsonify({
            'success': True,
            'country': country.upper(),
            'data': charts
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
