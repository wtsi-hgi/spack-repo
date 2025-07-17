# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlgem(RPackage):
    """Detect differential expression in microarray and proteomics datasets with the Power Law Global Error Model (PLGEM)

    The Power Law Global Error Model (PLGEM) has been shown to faithfully model the variance-versus-mean dependence that exists in a variety of genome-wide datasets, including microarray and proteomics data. The use of PLGEM has been shown to improve the detection of differentially expressed genes or proteins in these datasets.
    """

    homepage = "http://www.genopolis.it"
    bioc = "plgem"

    version("1.80.0", commit="67c49dad253a33a166a08895d91f704940840cc0")
    version("1.74.0", commit="57166e6c2c9a1f56b80bcbd1065f63824b46d08c")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
