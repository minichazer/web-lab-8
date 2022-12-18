from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Spitz, TypesSpitz


class SpitzSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return Spitz.objects.all()
    
    def lastmod(self, obj):
        return obj.lastedit_date

    def location(self, item):
        return reverse(item)


class SpitzTypesSitemap(Sitemap):
    priority = 0.3
    changefreq = 'daily'

    def items(self):
        return TypesSpitz.objects.all()
    
    def lastmod(self, obj):
        return obj.lastedit_date

    def location(self, item):
        return reverse(item)







# class StaticViewSitemap(Sitemap):
#     changefreq = 'daily'

#     def items(self):
#         return ['about', 'types', 'home']

#     def location(self, item):
#         return reverse(item)

#     # def lastmod(self, item):
#     #     return item.date




# class DynamicViewSitemap(Sitemap):
#     changefreq = 'daily'

#     def items(self):
#         return SiteMapModel.objects.all().order_by('id')

#     def location(self, item):
#         return f'/types/{item.pk}/'


    # def lastmod(self, item):
    #     return item.date