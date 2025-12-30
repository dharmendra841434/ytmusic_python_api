# YouTube Music API Backend

A Flask-based REST API backend that provides access to YouTube Music functionality using the `ytmusicapi` library. This backend allows you to search for music, retrieve song details, get streaming URLs, browse albums, artists, playlists, and more.

## Features

- 🔍 **Search** - Search for songs, albums, artists, playlists, and videos
- 🎵 **Songs** - Get song details and streaming URLs
- 💿 **Albums** - Retrieve album information and track listings
- 🎤 **Artists** - Get artist details, songs, and albums
- 📝 **Playlists** - Access playlist details and tracks
- 🏠 **Browse** - Get home feed recommendations and music charts
- 📜 **Lyrics** - Retrieve song lyrics
- 🌐 **CORS Enabled** - Ready for frontend integration

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone or navigate to the project directory:**

   ```bash
   cd c:\Users\dhruv\Desktop\Website\ytmusic_backend
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Create environment file:**
   ```bash
   copy .env.example .env
   ```
   Edit `.env` if you need to change default settings.

## Running the Server

Start the Flask development server:

```bash
python app.py
```

The server will start on `http://localhost:5000` by default.

## API Endpoints

### Health Check

**GET** `/api/health`

Check if the API is running.

**Response:**

```json
{
  "status": "healthy",
  "service": "YouTube Music API",
  "version": "1.0.0"
}
```

---

### Search

**GET** `/api/search`

Search for songs, albums, artists, or playlists.

**Query Parameters:**

- `query` (required) - Search query string
- `filter` (optional) - Filter type: `songs`, `albums`, `artists`, `playlists`, `videos`
- `limit` (optional) - Number of results (default: 20)

**Example:**

```bash
curl "http://localhost:5000/api/search?query=imagine%20dragons&filter=songs&limit=10"
```

**Response:**

```json
{
  "success": true,
  "query": "imagine dragons",
  "filter": "songs",
  "count": 10,
  "results": [...]
}
```

---

### Song Details

**GET** `/api/song/<video_id>`

Get detailed information about a song.

**Example:**

```bash
curl "http://localhost:5000/api/song/dQw4w9WgXcQ"
```

**Response:**

```json
{
  "success": true,
  "videoId": "dQw4w9WgXcQ",
  "data": {
    "videoDetails": {...},
    "streamingData": {...}
  }
}
```

---

### Song Streaming URL

**GET** `/api/song/<video_id>/stream`

Get streaming URLs for a song.

**Example:**

```bash
curl "http://localhost:5000/api/song/dQw4w9WgXcQ/stream"
```

**Response:**

```json
{
  "success": true,
  "videoId": "dQw4w9WgXcQ",
  "audioFormats": [...],
  "expiresInSeconds": "21540"
}
```

---

### Album Details

**GET** `/api/album/<browse_id>`

Get album information and track listing.

**Example:**

```bash
curl "http://localhost:5000/api/album/MPREb_1234567890"
```

---

### Artist Details

**GET** `/api/artist/<browse_id>`

Get artist information, songs, and albums.

**Example:**

```bash
curl "http://localhost:5000/api/artist/UCabcdefghijklmnop"
```

**GET** `/api/artist/<browse_id>/albums`

Get all albums from an artist.

---

### Playlist Details

**GET** `/api/playlist/<playlist_id>`

Get playlist information and tracks.

**Query Parameters:**

- `limit` (optional) - Number of tracks (default: 100)

**Example:**

```bash
curl "http://localhost:5000/api/playlist/RDCLAK5uy_1234567890?limit=50"
```

---

### Home Feed

**GET** `/api/home`

Get home feed with recommendations and trending content.

**Example:**

```bash
curl "http://localhost:5000/api/home"
```

---

### Music Charts

**GET** `/api/charts`

Get music charts (default country).

**GET** `/api/charts/<country>`

Get music charts for a specific country (e.g., US, GB, IN).

**Example:**

```bash
curl "http://localhost:5000/api/charts/US"
```

---

### Lyrics

**GET** `/api/lyrics/<browse_id>`

Get lyrics for a song. The browse ID is obtained from song details.

**Example:**

```bash
curl "http://localhost:5000/api/lyrics/MPLYt_1234567890"
```

---

## Usage Examples

### JavaScript (Fetch API)

```javascript
// Search for songs
async function searchSongs(query) {
  const response = await fetch(
    `http://localhost:5000/api/search?query=${encodeURIComponent(
      query
    )}&filter=songs`
  );
  const data = await response.json();
  return data.results;
}

// Get song details
async function getSongDetails(videoId) {
  const response = await fetch(`http://localhost:5000/api/song/${videoId}`);
  const data = await response.json();
  return data.data;
}

// Get streaming URL
async function getStreamUrl(videoId) {
  const response = await fetch(
    `http://localhost:5000/api/song/${videoId}/stream`
  );
  const data = await response.json();
  return data.audioFormats[0].url; // Get first audio format
}
```

### Python (Requests)

```python
import requests

# Search for songs
def search_songs(query):
    response = requests.get(
        'http://localhost:5000/api/search',
        params={'query': query, 'filter': 'songs'}
    )
    return response.json()['results']

# Get song details
def get_song_details(video_id):
    response = requests.get(f'http://localhost:5000/api/song/{video_id}')
    return response.json()['data']
```

## Configuration

Edit the `.env` file to configure:

- `FLASK_ENV` - Set to `development` or `production`
- `PORT` - Server port (default: 5000)
- `CORS_ORIGINS` - Allowed CORS origins (default: \*)

## Authentication (Optional)

For accessing personal library features (liked songs, personal playlists), you need to set up authentication:

1. Follow the [ytmusicapi authentication guide](https://ytmusicapi.readthedocs.io/en/stable/setup/browser.html)
2. Save the authentication headers to `headers_auth.json`
3. Update `.env` with `AUTH_HEADERS_PATH=headers_auth.json`
4. Modify `app.py` to use authenticated client:
   ```python
   ytmusic = YTMusic('headers_auth.json')
   ```

## Error Handling

All endpoints return errors in the following format:

```json
{
  "error": "Error message description"
}
```

Common HTTP status codes:

- `200` - Success
- `400` - Bad request (missing or invalid parameters)
- `404` - Endpoint not found
- `500` - Internal server error

## Development

### Project Structure

```
ytmusic_backend/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── routes/               # API route modules
    ├── __init__.py
    ├── search.py         # Search endpoints
    ├── songs.py          # Song endpoints
    ├── albums.py         # Album endpoints
    ├── artists.py        # Artist endpoints
    ├── playlists.py      # Playlist endpoints
    ├── browse.py         # Browse/home/charts endpoints
    └── lyrics.py         # Lyrics endpoints
```

## Deployment

Ready to deploy your API to production? Check out the comprehensive [Deployment Guide](DEPLOYMENT.md) for step-by-step instructions on deploying to:

- **Render** (Recommended) - Best for Flask applications
- **Vercel** - Serverless deployment option
- **Railway** - Alternative with generous free tier

The deployment guide includes:

- Complete setup instructions for each platform
- Environment variable configuration
- Troubleshooting tips
- Production best practices

## License

This project is for educational purposes. Please respect YouTube's Terms of Service when using this API.

## Contributing

Feel free to submit issues and enhancement requests!

## Resources

- [ytmusicapi Documentation](https://ytmusicapi.readthedocs.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)
