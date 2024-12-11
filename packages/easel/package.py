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
#     spack install easel
#
# You can edit this file again by typing:
#
#     spack edit easel
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Easel(AutotoolsPackage):
    """A C library for biological sequence analysis."""

    homepage = "https://github.com/EddyRivasLab/easel"
    url = "https://github.com/EddyRivasLab/easel/archive/refs/tags/easel-0.49.tar.gz"

    license("BSD")

    version("0.49", sha256="90f75bc4727e6dfb5f402d9f70cf4a606d9639f72d21e07461279d3f3f06b918")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
