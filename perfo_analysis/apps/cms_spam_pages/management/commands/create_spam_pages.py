from optparse import  make_option

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.webdesign.lorem_ipsum import paragraphs


from cms.api import create_page, add_plugin, publish_page
from cms.models.pagemodel import Page
from cms.plugin_pool import plugin_pool


class Command(BaseCommand):
    help = 'Generates spam pages'

    option_list = BaseCommand.option_list + (
        make_option("--page-num", dest="page-num", default=10),
        make_option("--plugin-num", dest="plugin-num", default=1),
        make_option("--depth", dest="depth", default=2),
        # default template is template_menu_1placeholder.html
        make_option("--template", dest="template",
                    default=settings.CMS_TEMPLATES[2][0])
,
    )

    def create_page(self, name, template,
            plugin_num=1, parent=None):
        lang = settings.LANGUAGES[0][0]
        created_by_user = "python-api"

        # Create page
        page = create_page(name, template,
                           lang,
                           created_by=created_by_user,
                           **{"parent": parent,
                               'in_navigation': True})
        self.add_lorem_text_plugins(page, plugin_num)
        return page

    def create_page_descendant(self, template, depth,
                               page_num, plugin_num, page=None):
        if depth > 0:
            for i in range(page_num):
                next_page = self.create_page('Page: %s - %s' % (str(i), str(depth)),
                                             template=template, plugin_num=plugin_num,
                                             parent=page)
                self.create_page_descendant(template, depth - 1,
                                            page_num, next_page)

    def get_html_lorem_paragraph(self, paragraph_num):
        html = ""
        for text in paragraphs(paragraph_num):
            html += '<p>%s</p>' % text
        return html

    def add_lorem_text_plugins(self, page, plugin_num):
        klass_text_plugin = plugin_pool.plugins['TextPlugin']
        available_placeholders = page.placeholders.all()
        for placeholder in available_placeholders:
            # Create plugins
            for i in range(plugin_num):
                add_plugin(placeholder, klass_text_plugin,
                            settings.LANGUAGES[0][0],
                            **{'body': self.get_html_lorem_paragraph(2)})

    def handle(self, *args, **options):
        try:
            page_num = int(options['page-num'])
            depth = int(options['depth'])
            template = options['template']
            plugin_num = options['plugin-num']
            for i in range(page_num):
                self.create_page_descendant(template, depth,
                                            page_num, plugin_num)

            #Publish the pages
            for page in Page.objects.drafts():
                user = User.objects.get(id=1)
                publish_page(page, user)
        except Exception, e:
            raise CommandError("There was an error running this command. ", e)
