from setuptools import setup, find_packages


version = '1.0.1'

with open('README.rst') as doc:
    long_description = doc.read()

setup(
    name='pygments-ldif',
    version=version,
    description='LDAP Data Interchange Format (LDIF) lexer for Pygments',
    long_description=long_description,
    author='Rob McBroom',
    author_email='pygments-ldif@skurfer.com',
    license='MIT License',
    url='http://projects.skurfer.com/posts/2011/ldif_pygments/',
    packages=find_packages(),
    install_requires=['Pygments'],
    py_modules=['ldif_lexer'],
    entry_points={'pygments.lexers': 'ldif=ldif_lexer:LdifLexer'}
)
