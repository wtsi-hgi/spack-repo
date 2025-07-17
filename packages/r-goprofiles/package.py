# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoprofiles(RPackage):
    """goProfiles: an R package for the statistical analysis of functional profiles

    The package implements methods to compare lists of genes based on comparing the corresponding 'functional profiles'.
    """

    bioc = "goProfiles"

    version("1.70.0", commit="57a92ca0f41ea58cb6d4a973a0d49271c07368b7")
    version("1.64.0", commit="a8fb44d5ba3e15648cd75ebe34bb06ea104acea5")

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-compquadform", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
