from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.viewlets.common import FooterViewlet

class hanghingFooterViewlet(FooterViewlet):
    index = ViewPageTemplateFile('templates/footer.pt')
