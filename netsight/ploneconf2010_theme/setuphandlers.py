def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('netsight.ploneconf2010_theme_various.txt') is None:
        return

    # Add additional setup code here

    from zope.component import getUtility
    from Products.CMFCore.interfaces import IPropertiesTool
    ptool = getUtility(IPropertiesTool)
    if ptool:
        try:
            stats_js = ptool.site_properties.webstats_js
            nag = unicode('<!-- NAGIOS COMMENT DO NOT DELETE -->')
            newline = unicode('\r\n')
            if nag not in stats_js:
                ptool.site_properties.webstats_js = stats_js + newline + nag

        except KeyError:
            print "Could not find Site Control Panel"
