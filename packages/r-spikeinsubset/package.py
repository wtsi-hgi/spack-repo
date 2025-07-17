# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpikeinsubset(RPackage):
    """Part of Affymetrix's Spike-In Experiment Data

    Includes probe-level and expression data for the HGU133 and HGU95 spike-in experiments
    """

    homepage = "https://bioconductor.org/packages/SpikeInSubset"
    bioc = "SpikeInSubset"

    version("1.48.0", commit="2413a3c0db1ac3be744e1758535d90b08c7dd832")
    version("1.42.0", commit="346a7b010a356762666aa4a0b7b9e5ac186518b9")

    depends_on("r@2.4:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
    depends_on("r-affy@1.23.4:", type=("build", "run"))
