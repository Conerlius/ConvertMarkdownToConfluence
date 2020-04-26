import pyperclip
import mistune
import MarkdownRenderer

class ActionClass:
    def SetWinHandle(self, handle):
        self._Handle = handle

    def UseTest(self, content):
        renderer = MarkdownRenderer.MarkdownRenderer()
        markdown = mistune.Markdown(renderer=renderer)
        return markdown(content)

    def Convert_To_Wiki(self):
        content = self._Handle.sources_text.get(0.0, 'end')
        result_text = self.UseTest(content)
        self._Handle.output_text.delete(0.0, 'end')
        self._Handle.output_text.insert(0.0, result_text)

    def Copy_To_Wiki(self):
        content = self._Handle.output_text.get(0.0, 'end')
        pyperclip.copy(content)