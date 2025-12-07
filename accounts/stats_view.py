from rest_framework import views, permissions, response
from django.contrib.auth import get_user_model
from orders.models import Order
from support.models import SupportTicket

User = get_user_model()

class AdminStatsView(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        total_revenue = sum(order.total_amount for order in Order.objects.all())
        total_orders = Order.objects.count()
        pending_orders = Order.objects.filter(status='Pending').count()
        active_users = User.objects.count()
        pending_tickets = SupportTicket.objects.filter(status='Open').count()

        data = {
            'total_revenue': total_revenue,
            'total_orders': total_orders,
            'pending_actions': pending_orders + pending_tickets,
            'active_users': active_users,
            'pending_orders': pending_orders,
            'pending_tickets': pending_tickets
        }
        return response.Response(data)
