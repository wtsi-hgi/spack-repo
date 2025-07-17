# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNullranges(RPackage):
    """Generation of null ranges via bootstrapping or covariate matching

    Modular package for generation of sets of ranges representing the null hypothesis. These can take the form of bootstrap samples of ranges (using the block bootstrap framework of Bickel et al 2010), or sets of control ranges that are matched across one or more covariates. nullranges is designed to be inter-operable with other packages for analysis of genomic overlap enrichment, including the plyranges Bioconductor package.
    """

    homepage = "https://nullranges.github.io/nullranges"
    bioc = "nullranges"

    version("1.14.0", commit="def76ef6ac12216b04a18a5134a519e4004b4dae")
    version("1.8.0", commit="7aa00490ae2ddf6239b244413cc4a22f166adbab")

    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-interactionset", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-plyranges", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-progress", type=("build", "run"))
    depends_on("r-ggridges", type=("build", "run"))
