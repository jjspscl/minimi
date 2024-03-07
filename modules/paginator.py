from django.core.paginator import Paginator
from django.core.paginator import Paginator


def is_htmx(request, boost_check=True):
    hx_boost = request.headers.get("Hx-Boosted")
    hx_request = request.headers.get("Hx-Request")

    if boost_check and hx_boost:
        print("Boosted")
        return False
    elif boost_check and not hx_boost and hx_request:
        return True


def paginate(request, qs, limit=2):
    paginator = Paginator(qs, limit)
    page_no = request.GET.get("page")
    return paginator.get_page(page_no)
