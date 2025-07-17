# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBobafit(RPackage):
    """Refitting diploid region profiles using a clustering procedure

    This package provides a method to refit and correct the diploid region in copy number profiles. It uses a clustering algorithm to identify pathology-specific normal (diploid) chromosomes and then use their copy number signal to refit the whole profile.  The package is composed by three functions: DRrefit (the main function), ComputeNormalChromosome and PlotCluster.
    """

    homepage = "https://github.com/andrea-poletti-unibo/BOBaFIT"
    bioc = "BOBaFIT"

    version("1.12.0", commit="4245ca046e5f5f662b06b05c51873a7773d27e1d")
    version("1.6.0", commit="2bac67f37e4ea8f30c43cb5447c950a5e21adb5e")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-nbclust", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggbio", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-ggforce", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-plyranges", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
