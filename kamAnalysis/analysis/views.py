from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Gap
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_gap(request, gap_id):
    print("Gap a borrar ", gap_id)
    gap_to = get_object_or_404(Gap, pk=gap_id)
    gap_to.delete()

    return HttpResponse(status=204)


@require_http_methods(["GET"])
def get_gaps(request):
    gap_query = Gap.objects.values().order_by('-date_selected')[:20]

    gap_list = []
    for item in gap_query:
        gap = {'id': item['id'], 'isClose': item['is_close'],
               'dateSelected': item['date_selected']}
        gap_list.append(gap)

    return JsonResponse(gap_list, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def add_gap(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print("Objecto python ", body)

    is_close, date_selected = body['isClose'], body['dateSelected']
    gap_add = Gap(is_close=is_close, date_selected=date_selected)
    gap_add.save()
    gap_query = Gap.objects.values().filter(date_selected=date_selected)

    gap_list = []
    for item in gap_query:
        gap = {'id': item['id'], 'isClose': item['is_close'],
               'dateSelected': item['date_selected']}
        gap_list.append(gap)

    return JsonResponse(gap_list[0], safe=False, status=201)
