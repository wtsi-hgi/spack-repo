# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProstatecancergrasso(RPackage):
    """Prostate Cancer Data

    A Bioconductor data package for the Grasso (2012) Prostate Cancer dataset.
    """

    bioc = "prostateCancerGrasso"

    version("1.36.0", commit="ce14be769393e0ccfca37b9758763f3ffc20c874")
    version("1.30.0", commit="ad1231283f04b129d629286b4d4f2b7a5b25c125")

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r@3.3:", type=("build", "run"))
