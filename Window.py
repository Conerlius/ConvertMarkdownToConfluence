from tkinter import *
import ToWiki

class Wind:
    def CreateWindow(self):
        self._action = ToWiki.ActionClass()
        self._action.SetWinHandle(self)
        self.root = Tk(className="Convert Markdown To Wiki")

        self.sources_text = Text(self.root)
        self.convert_btn = Button(self.root, text="Convert", command=self._action.Convert_To_Wiki)
        self.output_text = Text(self.root)
        self.copy_btn = Button(self.root, text="Copy", command=self._action.Copy_To_Wiki)
        #self.output_text.

        self.sources_text.pack()                    # 将小部件放置到主窗口中
        self.convert_btn.pack()
        self.output_text.pack()
        self.copy_btn.pack()

        self.root.mainloop()                 # 进入消息循环