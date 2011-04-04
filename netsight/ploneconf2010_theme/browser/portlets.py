from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.portlets.navigation import Renderer as PloneNavigationRender

from plone.app.portlets.portlets import base
from zope.interface import implements
from zope.formlib import form
from plone.portlets.interfaces import IPortletDataProvider

class NavigationRenderer(PloneNavigationRender):
    recurse = ViewPageTemplateFile('templates/navigation_recurse.pt')


class IHandyPortlet(IPortletDataProvider):
    """ Handy Interface """


class HandyAssignment(base.Assignment):
    implements(IHandyPortlet)

    @property
    def title(self):
        return u"Handy"


class HandyRenderer(base.Renderer):

    render = ViewPageTemplateFile('templates/handy_portlet.pt')
    
    @property
    def available(self):
        return True

    def getPlatinumSponsor(self): 
        brains  = self.context.portal_catalog.searchResults(
            meta_type = 'Sponsor',
            getSponsorshipLevel = 'platinum',
            )

        if brains:
            return brains[0]
    
class HandyAddForm(base.AddForm):
    form_fields = form.Fields(IHandyPortlet)
    label = u"Add Handy Portlet"
    description="A portlet to hold the column open and show a hand"

    def create(self, data):
        assignment = Assignment()
        return assignment
