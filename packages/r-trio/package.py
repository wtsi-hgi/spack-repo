# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrio(RPackage):
    """Testing of SNPs and SNP Interactions in Case-Parent Trio Studies

    Testing SNPs and SNP interactions with a genotypic TDT. This package furthermore contains functions for computing pairwise values of LD measures and for identifying LD blocks, as well as functions for setting up matched case pseudo-control genotype data for case-parent trios in order to run trio logic regression, for imputing missing genotypes in trios, for simulating case-parent trios with disease risk dependent on SNP interaction, and for power and sample size calculation in trio data.
    """

    bioc = "trio"

    version("3.46.0", commit="db20b0d0ebb4bb6271412ea654de1b05b892ce43")
    version("3.40.0", commit="ac9d1724dcc5701a1fba033e8aaa94882719880a")

    depends_on("r@3.0.1:", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-siggenes", type=("build", "run"))
    depends_on("r-logicreg@1.6.1:", type=("build", "run"))
