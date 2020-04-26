import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

class MarkdownRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        tag="javascript"
        if not lang:
            tag=lang
        return '\n{code:language=%s|borderStyle=solid|theme=RDark|linenumbers=true|collapse=false}\n %s \
\n{code}\n' %(tag, code)

    def header(self, text, level, raw=None):
        return 'h%s. %s\n' %(level, text)

    def list(self, body, ordered=True):
        tag = '\n'
        return '\n%s\n' % (body)

    def list_item(self, text):
        return '- %s\n' %text

    def block_quote(self, text):
        return '\n{quote}\n%s\n{quote}\n' % text.rstrip('\n')

    # strong
    def double_emphasis(self, text):
        return ' *%s* ' %text

    # 斜体
    def emphasis(self, text):
        return ' _%s_ ' % text

    # `code`
    def codespan(self, text):
        return ' {{%s}} ' % text

    # 删除线
    def strikethrough(self, text):
        return ' -%s- ' % text

    # image
    def image(self, src, title, text):
        return '!%s!' % src

    # link
    def autolink(self, link, is_email=False):
        if is_email:
            link = 'mailto:%s' % link
        return ' [link|%s] ' % (link)

    def link(self, link, title, text):
        if not text:
            return self.autolink(link, False)
        return '["%s"|"%s"]' % (text, link)


    def paragraph(self, text):
        return '%s\n' % text.strip(' ')