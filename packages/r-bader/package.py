# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBader(RPackage):
    """Bayesian Analysis of Differential Expression in RNA Sequencing Data

    For RNA sequencing count data, BADER fits a Bayesian hierarchical model. The algorithm returns the posterior probability of differential expression for each gene between two groups A and B. The joint posterior distribution of the variables in the model can be returned in the form of posterior samples, which can be used for further down-stream analyses such as gene set enrichment.
    """

    bioc = "BADER"

    version("1.46.0", commit="74b73591f21fd33ea77f807849398315a991a7d3")
    version("1.40.0", commit="a9aada30b45fe055764acd2ab414f947afcb6aba")
