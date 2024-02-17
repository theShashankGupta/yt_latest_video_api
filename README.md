# YouTube Latest Video API

This Flask project provides an API to fetch the latest videos from YouTube for a given tag/search query and store them in a database. It also includes a GET API for retrieving the stored video data in a paginated response.

## Basic Requirements

- Server continuously calls the YouTube API in the background with an interval for fetching the latest videos.
- Videos are stored in a database with fields including video title, description, publishing datetime, thumbnails URLs, etc.
- GET API returns the stored video data in a paginated response sorted by publishing datetime.

## Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/theShashankGupta/yt_latest_video_api.git
   cd yt_latest_video_api
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   . venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
   
   
