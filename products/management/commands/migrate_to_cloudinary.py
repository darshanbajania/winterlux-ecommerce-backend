import os
import cloudinary.uploader
from django.core.management.base import BaseCommand
from django.conf import settings
from products.models import Product

class Command(BaseCommand):
    help = 'Uploads local images to Cloudinary and updates database URLs'

    def handle(self, *args, **kwargs):
        # Path to frontend images
        # Assuming frontend is at ../test_project/public/images relative to backend root
        frontend_images_dir = os.path.join(settings.BASE_DIR, '../test_project/public')

        products = Product.objects.all()
        for product in products:
            image_path = product.image
            
            # Check if it's a local path (starts with /images/)
            if image_path and image_path.startswith('/images/'):
                # Construct full local path
                # Remove leading slash to join correctly
                relative_path = image_path.lstrip('/')
                full_path = os.path.join(frontend_images_dir, relative_path)
                
                if os.path.exists(full_path):
                    self.stdout.write(f'Uploading {product.name} image: {full_path}...')
                    
                    try:
                        # Upload to Cloudinary
                        # use filename as public_id for cleaner URLs
                        filename = os.path.splitext(os.path.basename(full_path))[0]
                        response = cloudinary.uploader.upload(
                            full_path, 
                            public_id=f"winterlux/{filename}",
                            overwrite=True
                        )
                        
                        # Update product with new secure URL
                        new_url = response['secure_url']
                        product.image = new_url
                        product.save()
                        
                        self.stdout.write(self.style.SUCCESS(f'Successfully updated {product.name} to {new_url}'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Failed to upload {full_path}: {str(e)}'))
                else:
                    self.stdout.write(self.style.WARNING(f'File not found: {full_path}'))
            else:
                self.stdout.write(f'Skipping {product.name}: Already remote or invalid path ({image_path})')
