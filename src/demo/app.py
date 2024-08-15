# Licensed under the GNU LGPL v3
# Copyright (C) 2024 numlinka.

import tkxml

handle: tkxml.TkXMLHandle
widget: tkxml.namespace.NamespaceWidget
variable: tkxml.namespace.NamespaceVariable


def bin_exit(*_):
    handle.mainwindow.destroy()

def bin_modify_variable(*_):
    variable.vcc.set("123")

def bin_modify_widget(*_):
    widget.hello_world.config(text="No Hello World")

def bin_hello_world(*_):
    print("Hello World")
