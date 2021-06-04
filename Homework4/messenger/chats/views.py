from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def chatList(request):
    return JsonResponse({'chat_list': [1, 2, 3]})


@require_http_methods(["GET"])
def chatDetail(request, chat_id):
    return JsonResponse({'status': 'ok', 'chat_id': chat_id})


@require_http_methods(["POST"])
def chatCreate(request, chat_id):
    return JsonResponse({'status': 'ok', 'chat_id': chat_id})