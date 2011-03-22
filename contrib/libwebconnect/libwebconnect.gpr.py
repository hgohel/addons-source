#------------------------------------------------------------------------
#
# Register the Addon
#
#------------------------------------------------------------------------

register(GENERAL,
         id="libwebconnect",
         name="libwebconnect",
         description = _("Library for web site collections"),
         status = STABLE,
         version = '1.0.6',
         gramps_target_version = "3.4",
         fname="libwebconnect.py",
         load_on_reg = True,
         )

