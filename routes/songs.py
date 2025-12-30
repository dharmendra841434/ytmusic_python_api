from flask import Blueprint, jsonify
from ytmusicapi import YTMusic

bp = Blueprint('songs', __name__)
ytmusic = YTMusic()

@bp.route('/api/song/<video_id>', methods=['GET'])
def get_song(video_id):
    """
    Get detailed information about a song
    Path params:
        - video_id: YouTube video ID
    """
    try:
        if not video_id:
            return jsonify({'error': 'Video ID is required'}), 400
        
        # Get song details
        song_info = ytmusic.get_song(video_id)
        
        return jsonify({
            'success': True,
            'videoId': video_id,
            'data': song_info
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/api/song/<video_id>/stream', methods=['GET'])
def get_stream_url(video_id):
    """
    Get streaming URL for a song
    Path params:
        - video_id: YouTube video ID
    """
    try:
        if not video_id:
            return jsonify({'error': 'Video ID is required'}), 400
        
        # Get song details which includes streaming info
        song_info = ytmusic.get_song(video_id)
        
        # Extract streaming formats
        streaming_data = song_info.get('streamingData', {})
        formats = streaming_data.get('adaptiveFormats', [])
        
        # Filter audio formats
        audio_formats = [f for f in formats if f.get('mimeType', '').startswith('audio')]
        
        return jsonify({
            'success': True,
            'videoId': video_id,
            'audioFormats': audio_formats,
            'expiresInSeconds': streaming_data.get('expiresInSeconds')
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
