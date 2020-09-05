# -*- coding: utf-8 -*-
"""Janela de diálogo personalizado com Gnome Builder."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./CustomDialog.glade')
class CustomDialog(Gtk.Dialog):
    __gtype_name__ = 'CustomDialog'

    entry = Gtk.Template.Child(name='entry')

    def __init__(self, parent):
        super().__init__()
        self.set_transient_for(parent=parent)

    def get_entry_text(self):
        return self.entry.get_text()


if __name__ == '__main__':
    custom_dialog = CustomDialog(parent=None)
    response = custom_dialog.run()
    print(response)
