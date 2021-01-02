# -*- coding: utf-8 -*-
"""Gtk.Button()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk


class Handler:

    def __init__(self):
        pass

    def on_button_clicked(self, widget):
        print('Botão pressionado.')


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='MainWindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()
