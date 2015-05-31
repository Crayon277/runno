from django.shortcuts import render

from django.http import Http404

from django.http import HttpResponse

from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response

from django.template import RequestContext

from django.core.context_processors import csrf

from unno.models import Blog, Author, Tag

from unno.forms import BlogForm, TagForm


def about(request):
    return render_to_response('about.html')

def resume(request):
    return render_to_response('resume.html')

def run(request):
    return render_to_response('just_run.html')

def unno(request):
    return render_to_response('unno.html',{})

def never_say_no(request):
    return render_to_response('never_say_no.html',{})


def now_or_never(request):
    return render_to_response('now_or_never.html',{})

def blog(requset):
    blog_list = Blog.objects.all()
    return render_to_response('blog_list.html',{"blogs":blog_list})

def blog_show(request,id=''):
    try:
        blog = Blog.objects.get(id = id)
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html",{'blog':blog})

def blog_filter(request, id = ''):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id = id)
    blogs = tag.blog_set.all()
    return render_to_response('blog_filter.html',{'blog':blogs, 'tag':tag, 'tags':tags})

def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            cd = form.cleaned_data
            cdtag = tag.cleaned_data

            tagname = cdtag['tagname']
            for taglist in tagname.split():
                Tag.objects.get_or_create(tag_name = taglist.strip())
            title = cd['caption']
            author = Author.objects.get(id = 1)
            content = cd['content']
            blog = Blog(caption = title, author = author, content = content)
            blog.save()
            for taglist in tagname.split():
                blog.tags.add(Tag.objects.get(tag_name = taglist.strip()))
                blog.save()
            id = Blog.objects.order_by('-publish_time')[0].id
            return HttpResponseRedirect('/blog/%s'%id)
    else:
        form = BlogForm()
        tag = TagForm(initial = {'tag_name':'notags'})
    return render_to_response('blog_add.html',{'form':form,'tag':tag},context_instance = RequestContext(request))

def blog_update(request, id = ''):
    id = id
    if request.method == 'POST':
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)

        if form.is_valid() and tag.is_valid():
            cd = form.cleaned_data
            cdtag = tag.cleaned_data

            tagname = cdtag['tag_name']
            tagnamelist = tagname.split()

            for taglist in tagnamelist:
                Tag.objects.get_or_create(tag_name = taglist.strip())

            title = cd['caption']
            content = cd['content']
            blog = Blog.objects.get(id = id)

            if blog:
                blog.caption = title
                blog.content = content
                blog.save()
                for taglist in tagnamelist:
                    blog.tags.add(Tag.objects.get(tag_name = taglist.strip()))

                tags = blog.tags.all()

                for tagname in tags:
                    tagname = unicode(str(tagname),'utf-8')
                    if tagname not in tagnamelist:
                        notag = blog.tags.get(tag_name = tagname)
                        blog.tags.remove(notag)
            else:
                blog = Blog(caption = blog.caption, content = blog.content)
                blog.save()
            return HttpResponseRedirect('/blog/%s'%id)
    else:
        try:
            blog = Blog.objects.get(id = id)
        except Exception:
            raise Http404
        form = BlogForm(initial = {'caption':blog.caption,'content':blog.content},auto_id=False)
        tags = blog.tags.all()
        if tags:
            taginit = ''
            for x in tags :
                taginit +=str(x)+' '
            tag = TagForm(initial = {'tag_name':taginit})
        else:
            tag = TagForm()
    return render_to_response('blog_add.html',{'form':form, 'id':id, 'tag':tag },context_instance = RequestContext(request))

def blog_del(request,id=''):
    try:
        blog = Blog.objects.get(id = id)
    except Exception:
        raise Http404
    if blog:
        blog.delete()
        return HttpResponseRedirect('/blog')
    blogs = Blog.objects.all()
    return render_to_response('blog_list.html',{'blogs':blogs})

# Create your views here.

def fire_work(request):
    return render_to_response('fire_work.html')
