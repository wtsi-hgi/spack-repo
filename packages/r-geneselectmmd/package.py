# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneselectmmd(RPackage):
    """Gene selection based on the marginal distributions of gene profiles that characterized by a mixture of three-component multivariate distributions

    Gene selection based on a mixture of marginal distributions.
    """

    bioc = "GeneSelectMMD"

    version("2.52.0", commit="8fd2d0b42414555270680b6ea29ef433c8159eae")
    version("2.46.0", commit="1000d0f9dc9841498a1281f4975df956af19eb69")

    depends_on("r@2.13.2:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
