from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='netsight.ploneconf2010_theme',
      version=version,
      description="This theme was built for PloneConfContentTypes",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='web zope plone theme',
      author='Netsight Internet Solutions Ltd',
      author_email='info@netsight.co.uk',
      url='ploneconf2010.org',
      license='Copyright Netsight Internet Solutions Ltd',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['netsight'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[],
      paster_plugins=[],
      )
