# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install fontforge
#
# You can edit this file again by typing:
#
#     spack edit fontforge
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Fontforge(CMakePackage):
    """FontForge is a free (libre) font editor for Windows, Mac OS X and GNU+Linux. Use it to create, edit and convert fonts in OpenType, TrueType, UFO, CID-keyed, Multiple Master, and many other formats."""

    homepage = "http://fontforge.org/"
    url = "https://github.com/fontforge/fontforge/archive/refs/tags/20230101.tar.gz"
    git = "https://github.com/fontforge/fontforge.git"

    license("GPL-3")

    version("20231231", commit="642d8a3db6d4bc0e70b429622fdf01ecb09c4c10")

    depends_on("libjpeg")
    depends_on("libtiff")
    depends_on("libpng")
    depends_on("freetype")
    depends_on("giflib")
    depends_on("gtkplus@3:")
    depends_on("libxml2")
    depends_on("pango")
    depends_on("cairo")
    depends_on("libspiro")
    depends_on("woff2")
    depends_on("python")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = [
            # "FREETYPE_LIBRARY={}".format(self.spec["freetype"].libs.directories[0]),
            # "FREETYPE_INCLUDE_DIRS={}".format(self.spec["freetype"].headers.directories[0]),
        ]
        return args
