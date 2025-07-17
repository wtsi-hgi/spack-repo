# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIchip(RPackage):
    """Bayesian Modeling of ChIP-chip Data Through Hidden Ising Models

    Hidden Ising models are implemented to identify enriched genomic regions in ChIP-chip data.  They can be used to analyze the data from multiple platforms (e.g., Affymetrix, Agilent, and NimbleGen), and the data with single to multiple replicates.
    """

    bioc = "iChip"

    version("1.62.0", commit="54e766613954f8b57a70af3b84d70a65d274ed44")
    version("1.56.0", commit="fed08be35bda6dad8adab04ab0e439bf3cddf7bf")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
