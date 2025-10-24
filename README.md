# AI Blog Application

A simple Django blog application with an API endpoint to create blog posts with images and content, plus web pages to list and view individual posts.

## Features

- 📝 **Create Blog Posts**: POST endpoint to create blog posts with base64-encoded images
- 📋 **List View**: Beautiful grid layout displaying all blog posts
- 🔍 **Detail View**: Individual post view with full content and metadata
- 🖼️ **Image Support**: Upload and display images with blog posts
- 🎨 **Modern UI**: Responsive design with gradient backgrounds and smooth animations

## Installation

1. **Activate the virtual environment**:
```bash
source env/bin/activate
```

2. **Install dependencies** (if not already installed):
```bash
pip install -r requirements.txt
```

3. **Run migrations** (already done):
```bash
python manage.py migrate
```

## Running the Application

Start the development server:
```bash
python manage.py runserver
```

The application will be available at:
- **List Page**: http://127.0.0.1:8000/
- **Create Endpoint**: http://127.0.0.1:8000/create
- **Browser Test Page**: http://127.0.0.1:8000/test/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## API Usage

### Create Blog Posts

**Endpoint**: `POST /create`

**Content-Type**: `application/json`

**Request Body**:
```json
[
  {
    "image": {
      "data": {
        "mimeType": "image/png",
        "fileType": "image",
        "fileExtension": "png",
        "data": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==",
        "fileName": "test_image",
        "fileSize": "1.5 MB"
      }
    },
    "content": "This is my first blog post! It has an image attached."
  },
  {
    "content": "This is a blog post without an image."
  }
]
```

**Note**: The `data` field should contain base64-encoded image data (without the `data:image/png;base64,` prefix, or with it - both work).

**Response** (201 Created):
```json
{
  "success": true,
  "message": "2 blog post(s) created",
  "posts": [
    {
      "id": 1,
      "content": "This is my first blog post! It has an image attached.",
      "image_url": "/media/blog_images/test_image.png",
      "created_at": "2025-10-24T12:00:00Z"
    },
    {
      "id": 2,
      "content": "This is a blog post without an image.",
      "image_url": null,
      "created_at": "2025-10-24T12:00:01Z"
    }
  ]
}
```

### Example cURL Command

```bash
curl -X POST http://127.0.0.1:8000/create \
  -H "Content-Type: application/json" \
  -d '[
    {
      "image": {
        "data": {
          "mimeType": "image/png",
          "fileType": "image",
          "fileExtension": "png",
          "data": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==",
          "fileName": "sample",
          "fileSize": "1 KB"
        }
      },
      "content": "Sample blog post with an image!"
    }
  ]'
```

## Web Pages

### Browser Test Page (NEW!)
Visit http://127.0.0.1:8000/test/ to create blog posts directly from your browser!

Features:
- Simple form interface
- Upload images from your computer
- Automatic base64 encoding
- Real-time success/error feedback
- Direct links to created posts

### List Page
Visit http://127.0.0.1:8000/ to see all blog posts in a beautiful grid layout.

Features:
- Grid layout with post cards
- Image previews
- Content preview (first 4 lines)
- Post metadata (ID, creation date)
- "Read More" button for each post

### Detail Page
Click on any blog post or visit http://127.0.0.1:8000/post/{id}/ to view the full post.

Features:
- Full post content
- Full-size image (if available)
- Complete metadata
- Back to list navigation

## Admin Panel

To access the admin panel and manage posts:

1. **Create a superuser**:
```bash
python manage.py createsuperuser
```

2. **Login**: Visit http://127.0.0.1:8000/admin/ and use your credentials

## Project Structure

```
aiblog/
├── aiblog/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── blog/                # Blog app
│   ├── models.py        # BlogPost model
│   ├── views.py         # API and page views
│   ├── urls.py          # URL routing
│   ├── admin.py         # Admin configuration
│   └── templates/       # HTML templates
│       └── blog/
│           ├── base.html
│           ├── post_list.html
│           └── post_detail.html
├── media/               # Uploaded images
│   └── blog_images/
├── manage.py
└── requirements.txt
```

## Technologies Used

- **Django 5.2.7**: Web framework
- **Pillow 12.0.0**: Image processing
- **SQLite**: Database (default)

## Notes

- The `/create` endpoint is CSRF-exempt for easy API access
- Images are stored in the `media/blog_images/` directory
- The application uses SQLite by default (file: `db.sqlite3`)
- Debug mode is enabled (suitable for development only)

