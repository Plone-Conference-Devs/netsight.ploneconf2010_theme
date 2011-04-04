from Products.Five import BrowserView
#from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone import Batch
from random import shuffle

class HomepageView(BrowserView):

    def getNewsItems(self):
         brains  = self.context.portal_catalog.searchResults(
             meta_type = 'PloneConfNewsItem',
             sort_on = 'Date',
             sort_order = 'reverse',
             )

         if brains:
             return list(brains)[:3]

         return None


    def getTalks(self):
         brains  = self.context.portal_catalog.searchResults(
             portal_type = 'netsight.ploneconf2010_talks.talk',
             )

         if brains:
             brains = list(brains)
             shuffle(brains)
             return [ b.getObject() for b in brains[:10] if b.Title != 'Open Space' ]

         return None


    def getPlatinumSponsor(self): 
        brains  = self.context.portal_catalog.searchResults(
            meta_type = 'Sponsor',
            getSponsorshipLevel = 'platinum',
            )

        if brains:
            return brains[0]


class PloneConfNewsItemFolderView(BrowserView):
    
    def getBatchedNewsItems(self):
        """return batching of news items within this folder, sorted in reverse order by date"""
        brains = self.context.portal_catalog.searchResults({
                'meta_type' : 'PloneConfNewsItem',
                'path' : '/'.join(self.context.getPhysicalPath()),
                'sort_on'   : 'Date',
                'sort_order' : 'reverse',
                'batch' : True,
                'b_size' : 10
                })

        return Batch(brains, 10, int(self.request.get('b_start', 0)), orphan=0)

