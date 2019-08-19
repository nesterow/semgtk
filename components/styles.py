import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


def load_css(ctx, filename):
    dirname = os.path.dirname(os.path.abspath(ctx))
    css = open(os.path.join(dirname,filename), "r").read()
    provider = Gtk.CssProvider()
    provider.load_from_data(str.encode(css))
    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )