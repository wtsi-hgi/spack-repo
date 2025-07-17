# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgfm(RPackage):
    """Marker Gene Finder in Microarray gene expression data

    The package is designed to detect marker genes from Microarray gene expression data sets
    """

    bioc = "MGFM"

    version("1.42.0", commit="86e6d46bebd07414dc91f4426f90f4b63d87376d")
    version("1.36.0", commit="8240478c1760217b4961a3ac596d9c2925d242b5")

    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-annotate", type=("build", "run"))
