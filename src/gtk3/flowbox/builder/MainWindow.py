# -*- coding: utf-8 -*-
"""Gtk.FlowBox()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gio, Gtk


@Gtk.Template(filename='MainWindow.ui')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    flowbox = Gtk.Template.Child(name='flowbox')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for n in range(100):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            self.flowbox.add(button)

        self.show_all()


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)


if __name__ == '__main__':
    import sys

    app = Application()
    app.run(sys.argv)
