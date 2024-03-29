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

3. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```


4. **Running the application:**
   ```sh
   python app.py
   ```

## API Endpoints

- GET /videos: Retrieves the stored video data in a paginated response.
- Start the Flask application.
- Use a tool like Postman to send requests to the API endpoint.
   ```sh
      http://localhost:5000/videos
   ```
- The default one will return the first page for next pages use ?page=page_no.
   ```sh
      http://localhost:5000/videos?page=2
   ```
