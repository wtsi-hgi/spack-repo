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
#     spack install atkmm
#
# You can edit this file again by typing:
#
#     spack edit atkmm
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Atkmm(MesonPackage):
    """atkmm is the C++ binding for the ATK library"""

    homepage = "https://github.com/GNOME/atkmm"
    url = "https://download.gnome.org/sources/atkmm/2.28/atkmm-2.28.4.tar.xz"

    license("LGPL-2.1")

    version("2.28.4", sha256="0a142a8128f83c001efb8014ee463e9a766054ef84686af953135e04d28fdab3")

    depends_on("atk")
    depends_on("cmake", type="build")
    depends_on("glibmm@2.66")
