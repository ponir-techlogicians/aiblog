# Quick Start Guide

## 1. Start the Server

```bash
cd /home/chizz/Documents/clients/jake/aiblog
source env/bin/activate
python manage.py runserver
```

## 2. Test the API

Run the test script to create sample posts:

```bash
python test_api.py
```

## 3. View Your Blog

Open your browser and visit:
- **List Page**: http://127.0.0.1:8000/
- **Post #1**: http://127.0.0.1:8000/post/1/
- **Post #2**: http://127.0.0.1:8000/post/2/
- **Post #3**: http://127.0.0.1:8000/post/3/

## 4. Create More Posts via API

Use curl or any HTTP client:

```bash
curl -X POST http://127.0.0.1:8000/create \
  -H "Content-Type: application/json" \
  -d '[{"content": "My awesome blog post!"}]'
```

## 5. Create Admin User (Optional)

To access the admin panel:

```bash
python manage.py createsuperuser
```

Then visit: http://127.0.0.1:8000/admin/

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | List all blog posts |
| `/post/<id>/` | GET | View individual post |
| `/create` | POST | Create new posts (API) |
| `/admin/` | GET | Admin panel |

## API Payload Format

```json
[
  {
    "image": {
      "data": {
        "mimeType": "image/png",
        "fileType": "image",
        "fileExtension": "png",
        "data": "BASE64_ENCODED_IMAGE_DATA",
        "fileName": "my_image",
        "fileSize": "1.5 MB"
      }
    },
    "content": "Your blog post content here"
  }
]
```

**Note**: The `image` field is optional. You can create posts with just content.

