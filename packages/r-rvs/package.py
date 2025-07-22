# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvs(RPackage):
    """Computes estimates of the probability of related individuals sharing a rare variant

    Rare Variant Sharing (RVS) implements tests of association and linkage between rare genetic variant genotypes and a dichotomous phenotype, e.g. a disease status, in family samples. The tests are based on probabilities of rare variant sharing by relatives under the null hypothesis of absence of linkage and association between the rare variants and the phenotype and apply to single variants or multiple variants in a region (e.g. gene-based test).
    """

    bioc = "RVS"

    version("1.30.0", commit="e83a9870b3d178f6b6eb5ca085c2be8c7cde9bdd")
    version("1.24.0", commit="8820b2211e512c22b3c76606663af9ef2b061bcb")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genlib", type=("build", "run"))
    depends_on("r-grain", type=("build", "run"))
    depends_on("r-snpstats", type=("build", "run"))
    depends_on("r-kinship2", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
