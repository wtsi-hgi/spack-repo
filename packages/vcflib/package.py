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
#     spack install vcflib
#
# You can edit this file again by typing:
#
#     spack edit vcflib
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Vcflib(CMakePackage):
    """A C++ library for parsing and manipulating VCF files."""

    homepage = "https://github.com/vcflib/vcflib"
    url = "https://github.com/vcflib/vcflib/archive/refs/tags/v1.0.10.tar.gz"
    git = "https://github.com/vcflib/vcflib.git"

    license("MIT")

    version("1.0.10", tag="v1.0.10", submodules=True)

    depends_on("htslib")
    depends_on("zig@:0.10")
    depends_on("py-pybind11")
