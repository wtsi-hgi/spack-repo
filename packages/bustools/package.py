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
#     spack install bustools
#
# You can edit this file again by typing:
#
#     spack edit bustools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Bustools(CMakePackage):
    """Tools for working with BUS files for single cell RNA-Seq datasets.
    
    bustools is a program for manipulating BUS files for single cell RNA-Seq 
    datasets. It can be used to error correct barcodes, collapse UMIs, produce 
    gene count or transcript compatibility count matrices, and is useful for 
    many other tasks."""

    homepage = "https://bustools.github.io/"
    url = "https://github.com/BUStools/bustools/archive/refs/tags/v0.45.1.tar.gz"

    license("BSD-2-Clause")

    version("0.45.1", sha256="d6b3ce8c700335aa10e28421da1edcedd3efa55e8390dd2729ff1d43ead0e642")

    # Dependencies based on CMake build system requirements
    depends_on("cmake@3.10:", type="build")
    depends_on("zlib-api", type=("build", "link"))

    def cmake_args(self):
        args = []
        return args
