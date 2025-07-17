# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeadarraysnp(RPackage):
    """Normalization and reporting of Illumina SNP bead arrays

    Importing data from Illumina SNP experiments and performing copy number calculations and reports.
    """

    bioc = "beadarraySNP"

    version("1.68.0", commit="569504fd9f04efa802b2d340053886ec5645feab")

    depends_on("r-biobase@2.14:", type=("build", "run"))
    depends_on("r-quantsmooth", type=("build", "run"))
