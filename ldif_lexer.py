"""
    pygments.lexers.ldif
    ~~~~~~~~~~~~~~

    Pygments lexer for LDAP Data Interchange Format.

    :copyright: (c) 2015 by Rob McBroom.
    :license: MIT, see LICENSE.txt for more details.
"""

from pygments.lexer import RegexLexer, bygroups
from pygments.token import *


class LdifLexer(RegexLexer):
    """Pygments lexer for LDAP Data Interchange Format."""
    name = 'LDAP Data Interchange Format'
    aliases = ['ldif', 'LDIF']
    filenames = ['*.ldif']
    tokens = {
        'root': [
            # authentication noise (not LDIF, but sent to STDOUT)
            (r'^SASL.*$', Text),
            # comments and in betweens
            (r'^#.*(\n .*){1,}$', Comment.Multiline),
            (r'^#.*$', Comment.Single),
            (r'^-$', Punctuation),
            (r'^(search|result|ref):\s.+$', Text),
            # attributes
            (r'^(add|replace|delete|replica|changetype)(?=:)',
             Keyword.Reserved),
            (r'^dn(?=:)', Name.Attribute, 'dn'),
            (r'^\w+(?=:)', Name.Attribute),
            # multiline values
            (r'(?<=:<\s).*(\n .*){1,}$', Name.Namespace),
            (r'(?<=::\s).*(\n .*){1,}$', Number.Hex),
            (r'(?<=:\s).*(\n .*){1,}$', Name.Variable),
            # values
            (r'(?<=changetype:\s)(add|modify|delete)$', Keyword.Reserved),
            (r'(?<=:\s)\d{14}(\.\d)?Z$', Number.Integer),
            (r'(?<=:<\s)\S.*$', String.Doc),
            (r'(?<=::\s)\S.*$', Number.Hex),
            (r'(?<=:\s)\S.*$', Name.Variable),
            # in-line separators
            (r'(?<=:)\s', Whitespace),
            (r'(?<=:<)\s', Whitespace),
            (r':[:<]?', Operator),
        ],
        'dn': [
            (r'(:)(\s)', bygroups(Operator, Whitespace)),
            (r'(?<=:\s).*(\n .*){1,}$', Name.Class),
            (r'(?<=:\s).*$', Name.Class),
        ],
    }
