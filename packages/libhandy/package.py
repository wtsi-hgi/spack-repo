# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Libhandy(MesonPackage):
    """The aim of the Handy library is to help with developing UI for mobile devices using GTK/GNOME."""

    homepage = "https://github.com/gnome/libhandy"
    url = "https://github.com/GNOME/libhandy/archive/refs/tags/1.8.3.tar.gz"

    version("1.8.3", sha256="7e7670f5d0a6d0adc24b888da44dab938a6f52472b8944d6dd4e31b6d3569a5f")

    depends_on("glib", type=("build", "run"))
    depends_on("pcre2", type=("build", "run"))
    depends_on("libffi", type=("build", "run"))
    depends_on("zlib", type=("build", "run"))
    depends_on("vala", type=("build", "run"))
    depends_on("pango", type=("build", "run"))
    depends_on("harfbuzz", type=("build", "run"))
    depends_on("freetype", type=("build", "run"))
    depends_on("bzip2", type=("build", "run"))
    depends_on("libpng", type=("build", "run"))
    depends_on("fribidi", type=("build", "run"))
    depends_on("fontconfig", type=("build", "run"))
    depends_on("libxml2", type=("build", "run"))
    depends_on("libxrender", type=("build", "run"))
    depends_on("xproto", type=("build", "run"))
    depends_on("renderproto")
    depends_on("libx11")
    depends_on("libxft")
    depends_on("libxi")
    depends_on("libepoxy")
    depends_on("cairo")
    depends_on("xrandr")
    depends_on("gdk-pixbuf")
    depends_on("atk")
    depends_on("at-spi2-atk")
    depends_on("gtkplus@3:", type=("build", "run"))
