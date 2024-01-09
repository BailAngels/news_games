from django.shortcuts import render

from apps.publishers.models import Publisher


def list_publishers(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher/list_publisher.html', locals())


def detail_publisher(request, pk):
    publisher = Publisher.objects.get(id=pk)
    return render(request, 'publisher/detail_publisher.html', locals())


