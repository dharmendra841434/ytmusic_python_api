from flask import request
from ytmusicapi import YTMusic
import os

# Logic to map common languages to their primary regions for better music recommendations
LANGUAGE_LOCATION_MAP = {
    'hi': 'IN',  # Hindi -> India
    'bn': 'IN',  # Bengali -> India
    'ta': 'IN',  # Tamil -> India
    'te': 'IN',  # Telugu -> India
    'ml': 'IN',  # Malayalam -> India
    'pa': 'IN',  # Punjabi -> India
    'gu': 'IN',  # Gujarati -> India
    'mr': 'IN',  # Marathi -> India
    'es': 'ES',  # Spanish -> Spain (Could also be MX, but ES is safe)
    'fr': 'FR',  # French -> France
    'de': 'DE',  # German -> Germany
    'ja': 'JP',  # Japanese -> Japan
    'ko': 'KR',  # Korean -> South Korea
    'pt': 'BR',  # Portuguese -> Brazil
    'ru': 'RU',  # Russian -> Russia
    'it': 'IT',  # Italian -> Italy
}

def get_ytmusic():
    """
    Returns a configured YTMusic instance based on request parameters or headers.
    """
    # Try to get language from query params 'lang' or 'language'
    lang = request.args.get('lang') or request.args.get('language')
    
    # If not in query params, try 'Accept-Language' header
    if not lang:
        accept_language = request.headers.get('Accept-Language')
        if accept_language:
            # Extract first language code (e.g., 'en-US,en;q=0.9' -> 'en')
            lang = accept_language.split(',')[0].split('-')[0].strip().lower()
    
    # Default to English if still not found
    if not lang:
        lang = os.getenv('DEFAULT_LANGUAGE', 'en')
    else:
        lang = lang.lower()

    # Try to get location/country from query params 'country' or 'location'
    country = request.args.get('country') or request.args.get('location')
    
    # Use language-to-location mapping if country is not provided
    if not country and lang in LANGUAGE_LOCATION_MAP:
        country = LANGUAGE_LOCATION_MAP[lang]
        
    # Default to US if still not found
    if not country:
        country = os.getenv('DEFAULT_LOCATION', 'US')

    
    # We always use 'en' for language to avoid translating the metadata (titles/headers)
    # as per user request, while the 'location' handles the regional music content.
    return YTMusic(language='en', location=country.upper())
