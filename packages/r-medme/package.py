# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedme(RPackage):
    """Modelling Experimental Data from MeDIP Enrichment

    MEDME allows the prediction of absolute and relative methylation levels based on measures obtained by MeDIP-microarray experiments
    """

    bioc = "MEDME"

    version("1.68.0", commit="3f2d1d9cfe25ed78de81caaaab165ae4004e2d61")
    version("1.62.0", commit="4158041f39ae364c45319599f4d9bddb91daf889")

    depends_on("r@2.15:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-drc", type=("build", "run"))
