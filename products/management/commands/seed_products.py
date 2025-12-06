from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Seeds the database with initial product data'

    def handle(self, *args, **kwargs):
        products_data = [
            {
                "id": "arctic-parka",
                "name": "Arctic Parka",
                "price": 299,
                "display_price": "$299",
                "color": "Midnight Blue",
                "image": "/images/parka.png",
                "description": "The ultimate winter companion. Our Arctic Parka features premium down insulation rated for extreme cold, a detachable fur-lined hood, and windproof outer shell. Designed for temperatures down to -30°C.",
                "features": ["Premium 800-fill down insulation", "Waterproof and windproof", "Adjustable fur-lined hood", "Multiple interior pockets"],
                "sizes": ["XS", "S", "M", "L", "XL", "XXL"],
                "slug": "arctic-parka"
            },
            {
                "id": "alpine-shell",
                "name": "Alpine Shell",
                "price": 189,
                "display_price": "$189",
                "color": "Glacier Grey",
                "image": "/images/shell.png",
                "description": "Lightweight yet incredibly protective. The Alpine Shell uses advanced technical fabrics to provide superior wind and water resistance while maintaining breathability for active winter adventures.",
                "features": ["3-layer waterproof membrane", "Fully taped seams", "Pit-zip vents", "Helmet-compatible hood"],
                "sizes": ["XS", "S", "M", "L", "XL", "XXL"],
                "slug": "alpine-shell"
            },
            {
                "id": "merino-layer",
                "name": "Merino Layer",
                "price": 89,
                "display_price": "$89",
                "color": "Charcoal",
                "image": "/images/layer.png",
                "description": "Experience the natural warmth of premium merino wool. This base layer regulates temperature, wicks moisture, and naturally resists odors for all-day comfort.",
                "features": ["100% Merino wool", "Temperature regulating", "Odor resistant", "Flatlock seams"],
                "sizes": ["XS", "S", "M", "L", "XL", "XXL"],
                "slug": "merino-layer"
            },
            {
                "id": "frost-boots",
                "name": "Frost Boots",
                "price": 249,
                "display_price": "$249",
                "color": "Black",
                "image": "/images/boots.png",
                "description": "Rugged winter boots built to last. Featuring waterproof leather construction, thermal insulation, and aggressive tread pattern for superior traction on ice and snow.",
                "features": ["Waterproof leather upper", "Thermal insulation", "Vibram Arctic Grip sole", "Removable liner"],
                "sizes": ["7", "8", "9", "10", "11", "12", "13"],
                "slug": "frost-boots"
            }
        ]

        for product_data in products_data:
            Product.objects.update_or_create(
                id=product_data['id'],
                defaults=product_data
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully seeded product "{product_data["name"]}"'))
