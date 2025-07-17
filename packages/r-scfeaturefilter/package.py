# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScfeaturefilter(RPackage):
    """A correlation-based method for quality filtering of single-cell RNAseq data

    An R implementation of the correlation-based method developed in the Joshi laboratory to analyse and filter processed single-cell RNAseq data. It returns a filtered version of the data containing only genes expression values unaffected by systematic noise.
    """

    bioc = "scFeatureFilter"

    version("1.28.0", commit="b87672fca6b47bdd87b9dd26ae5f29ad5441002d")
    version("1.22.0", commit="be3a47590b3ed63451e424042314987525c0b3f0")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-dplyr@0.7.3:", type=("build", "run"))
    depends_on("r-ggplot2@2.1:", type=("build", "run"))
    depends_on("r-magrittr@1.5:", type=("build", "run"))
    depends_on("r-rlang@0.1.2:", type=("build", "run"))
    depends_on("r-tibble@1.3.4:", type=("build", "run"))
