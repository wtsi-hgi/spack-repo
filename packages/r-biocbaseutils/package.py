# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocbaseutils(RPackage):
    """General utility functions for developing Bioconductor packages

    The package provides utility functions related to package development. These include functions that replace slots, and selectors for show methods. It aims to coalesce the various helper functions often re-used throughout the Bioconductor ecosystem.
    """

    bioc = "BiocBaseUtils"

    version("1.10.0", commit="af524da83589d37e1455ee1194efdfc3cafca0e5")
    version("1.4.0", commit="441d95a4e83f0d5eb6f016cd355bcc155ec69369")

    depends_on("r@4.2:", type=("build", "run"))
