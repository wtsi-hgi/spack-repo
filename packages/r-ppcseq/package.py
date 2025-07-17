# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpcseq(RPackage):
    """Probabilistic Outlier Identification for RNA Sequencing Generalized Linear Models

    Relative transcript abundance has proven to be a valuable tool for understanding the function of genes in biological systems. For the differential analysis of transcript abundance using RNA sequencing data, the negative binomial model is by far the most frequently adopted. However, common methods that are based on a negative binomial model are not robust to extreme outliers, which we found to be abundant in public datasets. So far, no rigorous and probabilistic methods for detection of outliers have been developed for RNA sequencing data, leaving the identification mostly to visual inspection. Recent advances in Bayesian computation allow large-scale comparison of observed data against its theoretical distribution given in a statistical model. Here we propose ppcseq, a key quality-control tool for identifying transcripts that include outlier data points in differential expression analysis, which do not follow a negative binomial distribution. Applying ppcseq to analyse several publicly available datasets using popular tools, we show that from 3 to 10 percent of differentially abundant transcripts across algorithms and datasets had statistics inflated by the presence of outliers.
    """

    homepage = "https://github.com/stemangiola/ppcseq"
    bioc = "ppcseq"

    version("1.16.0", commit="0caced2cd006b933f16dd927b8ec941999ac5fe8")
    version("1.10.0", commit="8195177a738d2b2d44a506f606771814db758b5f")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-rstan@2.18.1:", type=("build", "run"))
    depends_on("r-benchmarkme", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-lifecycle", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rcpp@0.12:", type=("build", "run"))
    depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-rstantools@2.1.1:", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidybayes", type=("build", "run"))
    depends_on("r-tidyr@0.8.3.9000:", type=("build", "run"))
    depends_on("r-bh@1.66:", type=("build", "run"))
    depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
    depends_on("r-stanheaders@2.18:", type=("build", "run"))
