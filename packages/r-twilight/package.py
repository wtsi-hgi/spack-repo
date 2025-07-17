# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwilight(RPackage):
    """Estimation of local false discovery rate

    In a typical microarray setting with gene expression data observed under two conditions, the local false discovery rate describes the probability that a gene is not differentially expressed between the two conditions given its corrresponding observed score or p-value level. The resulting curve of p-values versus local false discovery rate offers an insight into the twilight zone between clear differential and clear non-differential gene expression. Package 'twilight' contains two main functions: Function twilight.pval performs a two-condition test on differences in means for a given input matrix or expression set and computes permutation based p-values. Function twilight performs a stochastic downhill search to estimate local false discovery rates and effect size distributions. The package further provides means to filter for permutations that describe the null distribution correctly. Using filtered permutations, the influence of hidden confounders could be diminished.
    """

    homepage = "http://compdiag.molgen.mpg.de/software/twilight.shtml"
    bioc = "twilight"

    version("1.84.0", commit="42aae855241eba57174869af6f28ab87e886cbe1")
    version("1.78.0", commit="29890f3f4fd0d92dcb5a8aee2accfe4614e8e6b9")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
