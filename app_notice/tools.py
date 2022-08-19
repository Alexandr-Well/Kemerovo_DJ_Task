from django.core.paginator import PageNotAnInteger, EmptyPage


def make_pagination(page, paginator):
    try:
        notice = paginator.page(page)
    except PageNotAnInteger:
        notice = paginator.page(1)
    except EmptyPage:
        notice = paginator.page(paginator.num_pages)
    return {
        'notice': notice,
        'paginator': paginator,
    }


if __name__ == '__main__':
    pass
