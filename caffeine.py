#!/usr/bin/python
import os
from gi.repository import Gio, GLib, Gtk, AppIndicator3 as AppIndicator

idle_delay = 0
enable_button = Gtk.MenuItem("Enable")
disable_button = Gtk.MenuItem("Disable")
indicator = None

def clear_idle_delay():
  global idle_delay
  gsettings = Gio.Settings.new("org.gnome.desktop.session")
  idle_delay = gsettings.get_value('idle-delay').get_uint32()
  gsettings.set_value('idle-delay', GLib.Variant.new_uint32(0))

def restore_idle_delay():
  global idle_delay
  gsettings = Gio.Settings.new("org.gnome.desktop.session")
  if idle_delay and not gsettings.get_value('idle-delay').get_uint32():
    gsettings.set_value('idle-delay', GLib.Variant.new_uint32(idle_delay))

def toggle(item):
  global enable_button, disable_button, indicator
  if indicator.get_status() == AppIndicator.IndicatorStatus.ATTENTION:
    indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    enable_button.show()
    disable_button.hide()
    restore_idle_delay()
  else:
    indicator.set_status(AppIndicator.IndicatorStatus.ATTENTION)
    enable_button.hide()
    disable_button.show()
    clear_idle_delay()

def quit(item):
  restore_idle_delay()
  Gtk.main_quit()

def setup_menu():
  global enable_button, disable_button
  menu = Gtk.Menu()
  # Enable button
  enable_button.connect('activate', toggle)
  enable_button.show()
  menu.append(enable_button)
  # Disable button
  disable_button.connect('activate', toggle)
  menu.append(disable_button)
  # Quit button
  quit_button = Gtk.MenuItem("Exit")
  quit_button.connect('activate', quit)
  quit_button.show()
  menu.append(quit_button)
  # ... and return
  return menu

def setup_indicator():
  project_path = os.path.split(os.path.realpath(__file__))[0]
  print project_path
  indicator = AppIndicator.Indicator.new(
    'Caffeine',
    os.path.join(project_path, "cupempty.png"),
    AppIndicator.IndicatorCategory.APPLICATION_STATUS
  )
  indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
  indicator.set_attention_icon(os.path.join(project_path, "cupfull.png"))
  indicator.set_menu(setup_menu())
  return indicator

if __name__ == "__main__":
  indicator = setup_indicator()
  Gtk.main()
