from optparse import  make_option

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.sites.models import Site
from django.template.loader import render_to_string


from cms.models.pagemodel import Page


class Command(BaseCommand):
    help = 'Get the page urls'

    option_list = BaseCommand.option_list + (
        make_option("--filename", dest="filename", default=""),
        # default template is template_menu_1placeholder.html
        make_option("--template", dest="template",
                    default="url_list.txt"),
        make_option("--domain-name",
                    dest='domain_name',
                    default=(Site.objects.get(id=settings.SITE_ID)
                                         .domain))
    )

    def get_published_pages(self):
        """Get the queriset of the published Pages"""
        return Page.objects.published()

    def get_string_urls(self, template=None,
                        extra_context=None):
        """Create a file containing the urls"""
        pages = self.get_published_pages()
        extra_context.update({'pages': pages})
        return render_to_string(template, extra_context)

    def handle(self, *args, **options):
        try:
            filename = options['filename']
            template = options['template']
            domain_name = options['domain_name']
            string_urls = self.get_string_urls(template,
                    extra_context={'domain_name': domain_name})
            if filename:
                with open(filename, 'w') as f:
                    f.write(string_urls)
            else:
                print(string_urls)
        except Exception, e:
            raise CommandError("There was an error running this command. ", e)
