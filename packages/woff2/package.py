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
#     spack install woff2
#
# You can edit this file again by typing:
#
#     spack edit woff2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Woff2(CMakePackage):
    """font compression reference code."""

    homepage = "https://github.com/google/woff2"
    url = "https://github.com/google/woff2/archive/refs/tags/v1.0.2.tar.gz"

    license("MIT")

    version("1.0.2", sha256="add272bb09e6384a4833ffca4896350fdb16e0ca22df68c0384773c67a175594")

    depends_on("brotli")
