from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from .models import BlogPost
import json
import base64

# Create your views here.

@csrf_exempt
def create_blog_posts(request):
    """
    API endpoint to create blog posts from JSON payload
    POST /create
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
    
    try:
        data = json.loads(request.body)
        
        if not isinstance(data, list):
            return JsonResponse({'error': 'Payload must be an array'}, status=400)
        
        created_posts = []
        
        for item in data:
            content = item.get('content', '')
            image_data = item.get('image', {}).get('data', {})
            
            # Create blog post
            blog_post = BlogPost(content=content)
            
            # Handle image if present
            if image_data and 'data' in image_data:
                try:
                    # Decode base64 image
                    image_base64 = image_data['data']
                    file_extension = image_data.get('fileExtension', 'png')
                    file_name = image_data.get('fileName', 'image')
                    
                    # Remove data URL prefix if present
                    if 'base64,' in image_base64:
                        image_base64 = image_base64.split('base64,')[1]
                    
                    image_bytes = base64.b64decode(image_base64)
                    
                    # Save image to model
                    blog_post.image.save(
                        f"{file_name}.{file_extension}",
                        ContentFile(image_bytes),
                        save=False
                    )
                except Exception as e:
                    # Continue without image if there's an error
                    pass
            
            blog_post.save()
            created_posts.append({
                'id': blog_post.id,
                'content': blog_post.content,
                'image_url': blog_post.image.url if blog_post.image else None,
                'created_at': blog_post.created_at.isoformat()
            })
        
        return JsonResponse({
            'success': True,
            'message': f'{len(created_posts)} blog post(s) created',
            'posts': created_posts
        }, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def blog_list(request):
    """
    List view to display all blog posts
    """
    posts = BlogPost.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def blog_detail(request, pk):
    """
    Detail view to display a single blog post
    """
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def api_test(request):
    """
    API test page to create blog posts from browser
    """
    return render(request, 'blog/api_test.html')
