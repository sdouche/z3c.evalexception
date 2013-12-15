from setuptools import setup, find_packages

setup(name='z3c.evalexception',
      version = '3.0',
      license='ZPL 2.1',
      description="Debugging middlewares for zope.publisher-based web "
      "applications",
      author='Philipp von Weitershausen',
      author_email='philipp@weitershausen.de',
      long_description=open('README.txt').read(),
      classifiers = ['Development Status :: 5 - Production/Stable',
                     'Environment :: Web Environment',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: Zope Public License',
                     'Programming Language :: Python',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.3',
                     'Topic :: Internet :: WWW/HTTP',
                     'Framework :: Zope3',
                     ],

      packages=find_packages(),
      namespace_packages=['z3c'],
      install_requires=['setuptools', 'WebError', 'zope.security'],
      zip_safe=True,
      entry_points="""
      [paste.filter_app_factory]
      main = z3c.evalexception:zope_eval_exception
      ajax = z3c.evalexception:zope_eval_exception
      pdb = z3c.evalexception:post_mortem_debug
      """
      )
