default_application = "splinterlink"
default_controller = "default"
default_function = "index"

routes_in = (
  ('/$c/$f', '/splinterlink/$c/$f'),
)

routes_out = (
  ('/splinterlink/$c/$f', '/$c/$f'),
)
