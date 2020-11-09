import uuid

from django.conf import settings
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import CommentForm, SubscriberForm, ContactForm
from .models import Post, Categorie, Comment, Subscriber, Contact
from registration.models import User


class AboutView(TemplateView):
    template_name = 'about.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'privacyPolicy.html'


class TermsOfServiceView(TemplateView):
    template_name = 'termsOfService.html'


class Search(View):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        query = request.GET['query']
        if len(query) > 60 or len(query) == 0:
            posts = []
        else:
            post_by_title = Post.objects.filter(
                title__icontains=query)
            post_by_category = Post.objects.filter(
                category__name__icontains=query)
            post_by_tag = Post.objects.filter(tags__icontains=query)
            all_posts = post_by_title.union(post_by_category, post_by_tag)

        if all_posts:
            post_per_page = Paginator(all_posts, 10)
            page_number = self.request.GET.get('page')
            posts = post_per_page.get_page(page_number)
        else:
            posts = []

        return render(request, self.template_name, {'posts': posts, 'query': query})


class CategoryPost(TemplateView):
    template_name = 'my_blog/categoryPost.html'

    def get_context_data(self, **kwargs):
        category_name = self.kwargs['slug'].replace("-", " ")
        all_posts = Post.objects.all().filter(
            category__name__iexact=category_name).order_by('-publish_date')

        context = super().get_context_data(**kwargs)
        post_per_page = Paginator(all_posts, 15)

        page_number = self.request.GET.get('page')
        posts = post_per_page.get_page(page_number)

        context['category_name'] = category_name

        if posts:
            context['posts'] = posts
        else:
            context['no_post'] = True

        return context


class PostPageView(View):
    template_name = 'my_blog/postPage.html'

    def get(self, request, *args, **kwargs):
        _id = kwargs['id']
        slug = kwargs['slug']
        post = get_object_or_404(Post, slug__iexact=slug)
        latest_posts = Post.objects.order_by(
            '-publish_date').exclude(title__iexact=post.title)
        related_category_post = Post.objects.filter(
            category__name__iexact=post.category).exclude(title__iexact=post.title)[:3]
        all_posts = Post.objects.all().order_by('-publish_date')

        '''
        Retrive all the comments from the post
        '''
        comments = Comment.objects.all().filter(
            post__postId=_id, isApprove=True)

        context_dict = {
            'post': post,
            'related_category_post': related_category_post,
            'form': CommentForm(),
            'comments': comments
        }

        return render(request, self.template_name, context_dict)

    def post(self, request, *args, **kwargs):
        '''
        Create Comments
        '''
        slug = kwargs['slug']

        post = get_object_or_404(Post, slug__iexact=slug)
        form_class = CommentForm

        if request.method == "POST":
            form = form_class(request.POST or None)
            if form.is_valid():

                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()

                messages.info(
                    request, 'Your comment is awaiting moderation', extra_tags='info')

                return redirect(request.path)

            return render(request, self.template_name, {'form': form})


class Home(View):
    def get(self, request, *args, **kwargs):

        categories = Categorie.objects.all()
        posts = Post.objects.all().order_by('-publish_date')

        context = {}
        category_list = []

        for category in categories:
            category_posts = Post.objects.all().filter(
                category__name__iexact=category).order_by('-publish_date')[:6]

            category_name = category.name.replace(" ", "")\
                if category.name.find(" ")\
                else category

            category_list.append({
                "posts": category_posts,
                "obj": category
            })

        context['categories'] = category_list
        context['posts'] = posts

        return render(request, 'my_blog/home.html', context)


class ContactFormView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        path = self.request.path
        is_contact_path = ('/contact/' == path)
        feedback_message_identifier = "contact with us" if is_contact_path else "feedback"

        form_data = form.save(commit=False)
        form_data.message_type = path[1:len(path) - 1]
        form_data.save()

        messages.info(
            self.request, f"Thank you for {feedback_message_identifier}. You'll recive a email from us shortly", extra_tags='info')

        return super().form_valid(form)


class EmailSubscription(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('subscriber_email')
        if email:
            subs = Subscriber(subscriber_email=email)
            subs.save()
            return redirect(request.GET['next'])

        else:
            return redirect(request.GET['next'])
