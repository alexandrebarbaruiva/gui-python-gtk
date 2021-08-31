# -*- coding: utf-8 -*-
"""Python e GTK 4: Adw.ApplicationWindow()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Gio, Gtk
from gi.repository import Adw


class MainWindow(Adw.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: Adw.ApplicationWindow()')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        # O seu código aqui:
        # ...


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
