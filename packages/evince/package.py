# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Evince(MesonPackage):
    """Evince is a document viewer capable of displaying multiple and single page document formats like PDF and Postscript."""

    homepage = "https://wiki.gnome.org/Apps/Evince"
    url = "https://download.gnome.org/sources/evince/48/evince-48.0.tar.xz"

    version("48.0", sha256="cd2f658355fa9075fdf9e5b44aa0af3a7e0928c55614eb1042b36176cf451126")

    depends_on("poppler+glib", type=("build", "run"))
    depends_on("gdk-pixbuf+tiff", type=("build", "run"))
    depends_on("jpeg")
    depends_on("libtiff")
    depends_on("gtkplus@3:")
    depends_on("libhandy")
    depends_on("gettext")
    depends_on("itstool")
    depends_on("py-gi-docgen", type=("build"))
    depends_on("desktop-file-utils", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-markdown", type=("build", "run"))
    depends_on("py-markupsafe", type=("build", "run"))
    depends_on("py-pygments", type=("build", "run"))
    depends_on("py-typogrify", type=("build", "run"))
    depends_on("py-toml", type=("build", "run"))

    def setup_run_environment(self, env):
        env.set("GSETTINGS_SCHEMA_DIR", self.prefix + "/share/glib-2.0/schemas")
