from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(r'^/?$', views.issue_form),
    url(r'^github_jira_sync$', views.github_jira_sync),
    url(r'^issue/submit/?$', views.make_issue),
    url(r'^subscriptions/?$', views.manage_subscriptions),
    url(r'^subscriptions/remove/?$', views.remove_subscription),
    url(r'^question/(\d+)/next$', views.get_next),
    url(r'^questions/create/?$', views.create_question),
    url(r'^questions/delete/(\d+)/?$', views.delete_question),
    url(r'^questions/category/(\d+)/?$', views.add_category_to_question),
    url(r'^sources/?$', views.show_sources),
    url(r'^sources/(\d+)/questions?$', views.show_question),
    url(r'^sources/add', views.source_add),
    url(r'^sources/(\d+)/edit', views.source_edit),
    url(r'^sources/(\d+)/issues', views.source_issues),
    url(r'^sources/(\d+)/remove', views.source_remove),
)
