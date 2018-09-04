from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from bookmarks.forms import SearchForm

def search_page(request):
    form = SearchForm()
    bookmarks = []
    show_results = False
    if 'query' in request.GET:
        show_results = True
        query = request.GET['query'].strip()
        if query:
            form = SearchForm({'query' : query})
            bookmarks = Bookmark.objects.filter( title__icontains=query)[:10]
    variables = RequestContext(request, {'form': form,'bookmarks': bookmarks,'show_results': show_results, 'show_tags': True, 'show_user': True })
    if request.GET.has_key('AJAX'):):):
        return render_to_response('bookmark_list.html', variables)
    else:
        return render_to_response('search.html', variables)

def _bookmark_save(request, form):
    # Create or get link.
    link, dummy = \
    Link.objects.get_or_create(url=form.clean_data['url'])
        # Create or get bookmark.
    bookmark, created = Bookmark.objects.get_or_create(
                                                           user=request.user,
                                                           link=link
                                                           )
            # Update bookmark title.
    bookmark.title = form.clean_data['title']
            # If the bookmark is being updated, clear old tag list.
    if not created:
            bookmark.tag_set.clear()
# Create new tag list.
    tag_names = form.clean_data['tags'].split()
    for tag_name in tag_names:
        tag, dummy = Tag.objects.get_or_create(name=tag_name)
        bookmark.tag_set.add(tag)
    # Save bookmark to database and return it.
        bookmark.save()
    return bookmark
    Now in the same file, replace the code that you removed from
    bookmark_save_page
    with a call to _bookmark_save :
        @login_required
        def bookmark_save_page(request):
            if request.method == 'POST':
                form = BookmarkSaveForm(request.POST)
            if form.is_valid():
                bookmark = _bookmark_save(request, form)
                return HttpResponseRedirect('/user/%s/' % request.user.username)
            else:
                form = BookmarkSaveForm()
                variables = RequestContext(request, {'form': form})
            return render_to_response('bookmark_save.html', variables)
