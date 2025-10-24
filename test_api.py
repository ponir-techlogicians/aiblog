#!/usr/bin/env python3
"""
Test script for the AI Blog /create endpoint
"""
import requests
import json
import base64
from io import BytesIO
from PIL import Image

def create_sample_image():
    """Create a simple test image and return it as base64"""
    # Create a simple 200x200 gradient image
    img = Image.new('RGB', (200, 200), color='white')
    pixels = img.load()
    
    for i in range(200):
        for j in range(200):
            # Create a gradient effect
            r = int(102 + (i / 200) * 100)  # 102-202
            g = int(126 + (j / 200) * 100)  # 126-226
            b = int(234 - (i / 200) * 50)   # 234-184
            pixels[i, j] = (r, g, b)
    
    # Convert to base64
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    img_bytes = buffer.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    
    return img_base64

def test_create_endpoint():
    """Test the /create endpoint with sample data"""
    
    print("🧪 Testing AI Blog /create endpoint...")
    print("-" * 60)
    
    # Create sample image
    print("📷 Generating sample image...")
    sample_image = create_sample_image()
    
    # Prepare payload
    payload = [
        {
            "image": {
                "data": {
                    "mimeType": "image/png",
                    "fileType": "image",
                    "fileExtension": "png",
                    "data": sample_image,
                    "fileName": "test_gradient",
                    "fileSize": "10 KB"
                }
            },
            "content": "🎨 This is a test blog post with a beautiful gradient image! The image was generated programmatically using Python and PIL."
        },
        {
            "content": "📝 This is a second test blog post without an image. It demonstrates that images are optional in the payload."
        },
        {
            "image": {
                "data": {
                    "mimeType": "image/png",
                    "fileType": "image",
                    "fileExtension": "png",
                    "data": sample_image,
                    "fileName": "another_test",
                    "fileSize": "10 KB"
                }
            },
            "content": "🚀 Third blog post! This one also has an image. The AI Blog application supports multiple posts in a single API call."
        }
    ]
    
    # Send request
    print("📤 Sending POST request to http://127.0.0.1:8000/create...")
    
    try:
        response = requests.post(
            'http://127.0.0.1:8000/create',
            json=payload,
            headers={'Content-Type': 'application/json'}
        )
        
        print(f"\n✅ Response Status: {response.status_code}")
        print("\n📋 Response Body:")
        print(json.dumps(response.json(), indent=2))
        
        if response.status_code == 201:
            print("\n" + "=" * 60)
            print("🎉 SUCCESS! Blog posts created successfully!")
            print("=" * 60)
            print("\n📍 Visit the following URLs to see your posts:")
            print("   • List page: http://127.0.0.1:8000/")
            for post in response.json().get('posts', []):
                print(f"   • Post #{post['id']}: http://127.0.0.1:8000/post/{post['id']}/")
        else:
            print("\n⚠️  Request failed. Check the response above for details.")
            
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Could not connect to the server.")
        print("   Make sure the Django development server is running:")
        print("   python manage.py runserver")
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")

if __name__ == '__main__':
    test_create_endpoint()

