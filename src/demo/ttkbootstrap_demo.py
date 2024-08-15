# Licensed under the GNU LGPL v3
# Copyright (C) 2024 numlinka.

# site
import tkxml
import ttkbootstrap

# local
import app


# 将 ttkbootstrap 插入到 misc_source 的第一位
tkxml.settings.misc_source.insert(0, ttkbootstrap)


class Interface (tkxml.TkXMLHandle):
    def initialization_first(self, *_) -> None:
        self.set_namespace(app)
        self.create_xml("test.xml")



interface = Interface()
interface.mainwindow.mainloop()
