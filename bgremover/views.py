from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rembg import remove  # Import from installed library

def bgremover(request):
    if request.method == 'POST':
        image = request.FILES['image']

        # Error handling for invalid file types:
        if not image.content_type.startswith('image/'):
            error_message = 'Please upload a valid image file (PNG or JPEG).'
            return render(request, 'bgremover.html', {'error_message': error_message})

        try:
            # Use RemoveBackground library for background removal
            image_without_background = remove(image.read())

            # Save the processed image to temporary storage
            temp_filename = f'removed_background_{image.name}'
            with default_storage.open(temp_filename, 'wb') as destination:
                destination.write(image_without_background)

            # Create a ContentFile object to pass to the template
            processed_image = f'/media/{temp_filename}'  # Update processed image URL
            return render(request, 'bgremover.html', {'result_image': processed_image})  # Pass processed image URL

        except Exception as e:
            error_message = f'Error removing background: {str(e)}'
            return render(request, 'bgremover.html', {'error_message': error_message})

    else:
        # Handle GET requests (initial form rendering)
        return render(request, 'bgremover.html')
