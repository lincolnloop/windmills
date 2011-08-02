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
        make_option("--depth", dest="depth", default=2),
    )

    def create_page(self, index, parent=None):
        name = 'Page %s' % str(index)
        tmpl = settings.CMS_TEMPLATES[0][0]
        lang = settings.LANGUAGES[0][0]
        created_by_user = "python-api"

        # Create page
        page = create_page(name, tmpl, lang,
                           created_by=created_by_user,
                           **{"parent": parent,
                               'in_navigation': True})
        return page

    def create_page_descendant(self, depth, page_num, page):
        if depth > 0:
            for i in range(page_num):
                next_page = self.create_page('%s - %s' % (str(i), str(depth)),
                                            parent=page)
                self.create_page_descendant(depth - 1, page_num, next_page)

    def get_html_lorem_paragraph(self, paragraph_num):
        html = ""
        for text in paragraphs(paragraph_num):
            html += '<p>%s</p>' % text
        return html

    def add_lorem_text_plugins(self, page):
        klass_text_plugin = plugin_pool.plugins['TextPlugin']
        available_placeholders = page.placeholders.all()
        for placeholder in available_placeholders:
            # Create plugin
            add_plugin(placeholder, klass_text_plugin,
                        settings.LANGUAGES[0][0],
                        **{'body': self.get_html_lorem_paragraph(2)})

    def handle(self, *args, **options):
        try:
            page_num = int(options['page-num'])
            depth = int(options['depth'])
            for i in range(page_num):
                page = self.create_page(index=i, parent=None)
                self.add_lorem_text_plugins(page)
                self.create_page_descendant(depth,
                                            page_num,
                                            page)

            #Publish the pages
            for page in Page.objects.drafts():
                user = User.objects.get(id=1)
                publish_page(page, user)
        except Exception, e:
            raise CommandError("There was an error running this command. ", e)
