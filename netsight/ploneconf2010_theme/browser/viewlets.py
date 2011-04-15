from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import PersonalBarViewlet, LogoViewlet, GlobalSectionsViewlet
from Products.PloneConfContentTypes.content.interfaces import IPloneConfFolder, IPloneConfNewsItemFolder

from zope.component import getMultiAdapter
from random import shuffle
from DateTime import DateTime

class Utilities:
    def atHome(self):
        portal_context_state = getMultiAdapter((self.context, self.request), name=u'plone_context_state')
        #isPortalRoot = portal_context_state.is_portal_root()
        viewTemplateId = portal_context_state.view_template_id()
        return viewTemplateId == '@@homepage_view'


class PersonalBar(PersonalBarViewlet):
    index = ViewPageTemplateFile('templates/personalbar_viewlet.pt')


class GlobalSections(GlobalSectionsViewlet):
    index = ViewPageTemplateFile('templates/sections_viewlet.pt')

    def getProgrammeBrain(self):
         brains  = self.context.portal_catalog.searchResults(
             meta_type = ['PloneConfFolder', 'PloneConfDocument'],
             sort_on = 'getObjPositionInParent',
             id = 'programme'
             )
         if brains:
             return list(brains)[0]
         return None       
        

class Logo(LogoViewlet, Utilities):
    def update(self):
        super(Logo, self).update()
        portal = self.portal_state.portal()
        bprops = portal.restrictedTraverse('base_properties', None) 
        if bprops is not None:
            logoName = bprops.logoName
        if self.atHome():
            logoName = 'logo_homepage.png'
        else:
            logoName = 'logo.png'
        self.logo_tag = portal.restrictedTraverse(logoName).tag()
        self.portal_title = self.portal_state.portal_title()


class SiteTitle(ViewletBase, Utilities):
    index = ViewPageTemplateFile('templates/sitetitle_viewlet.pt')


class SponsorTickets(ViewletBase):
    index = ViewPageTemplateFile('templates/sponsortickets_viewlet.pt')

    def getHomepage(self):
         brains  = self.context.portal_catalog.searchResults(
             meta_type = 'Homepage',
             sort_on = 'Date',
             sort_order = 'reverse',
             )
         if brains:
             return list(brains)[0]
         return None

    def isEarlybirdAvailable(self):
        homepage = self.getHomepage()
        
        if homepage:
            if homepage['getEarlybirdCutOff'] > DateTime():
                return True
        return False


class SectionTitle(ViewletBase, Utilities):
    index = ViewPageTemplateFile('templates/sectiontitle_viewlet.pt')

    def getSection(self):
        context = self.context
        sectionpath = '/'.join(context.getPhysicalPath()[:3])
        try:
            section = context.restrictedTraverse(sectionpath)
        except:
            return None
        avail = IPloneConfFolder.providedBy(section) or IPloneConfNewsItemFolder.providedBy(section)
        if avail:
            return section
        return None
        

class BorderAboveContent(ViewletBase, Utilities):
    pass


class BorderBelowContent(ViewletBase, Utilities):
    pass


class Sponsors(ViewletBase, Utilities):
    def getSponsorsByCategory(self):
        categories = ['gold', 'silver', 'bronze', 'supporting',]
        brains  = self.context.portal_catalog.searchResults(
            meta_type = 'Sponsor',
            )
        list=[]
        for cat in categories:
            temp = []
            if brains:
                temp = [x for x in brains if x['getSponsorshipLevel'] == cat]
                shuffle(temp)
            list.append({'name':cat, 'sponsors':temp})
        return list


class Footer(ViewletBase, Utilities):
    index = ViewPageTemplateFile('templates/footer_viewlet.pt')

    def getTabs(self, brain=None):
        if not brain:
            portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
            portal = portal_state.portal()
            portal_path = '/'.join(portal.getPhysicalPath())
            query = {
                'path':{'query':portal_path, 'depth':1},
                'sort_on': 'getObjPositionInParent'
            }
        if brain:
            query = {
                'path':{'query':brain.getPath(), 'depth':1},
                'sort_on': 'getObjPositionInParent'
                }
        brains  = self.context.portal_catalog.searchResults(query)
        ignores= ['Homepage', 'netsight.conferencetalks.talk']
        brains = [x for x in brains if not (x['exclude_from_nav'] or x['portal_type'] in ignores)]
        return brains
        
