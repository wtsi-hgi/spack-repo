# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaresim(RPackage):
    """Simulation of Rare Variant Genetic Data

    Haplotype simulations of rare variant genetic data that emulates real data can be performed with RAREsim. RAREsim uses the expected number of variants in MAC bins - either as provided by default parameters or estimated from target data - and an abundance of rare variants as simulated HAPGEN2 to probabilistically prune variants. RAREsim produces haplotypes that emulate real sequencing data with respect to the total number of variants, allele frequency spectrum, haplotype structure, and variant annotation.
    """

    homepage = "https://github.com/meganmichelle/RAREsim"
    bioc = "RAREsim"

    version("1.12.0", commit="ade75ecbdf4b55424b39885c5a43a244389b03c1")
    version("1.6.0", commit="7e18d5764e1846ec7d3abddcf5d7600ac191083d")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-nloptr", type=("build", "run"))
