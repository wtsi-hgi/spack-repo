# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigfit(RPackage):
    """Flexible Bayesian inference of mutational signatures

    Implements Bayesian models for fitting and extracting mixtures of
    mutational signatures from mutation count data. Provides interfaces to
    four different Bayesian signature models (multinomial, Poisson, normal
    and negative binomial), as well as auxiliary functions for analysing and
    plotting resulting data. Markov chain Monte Carlo sampling is performed
    using Stan.
    """

    homepage = "https://github.com/kgori/sigfit"
    url = "https://github.com/kgori/sigfit/archive/refs/tags/v2.2.0.tar.gz"

    # Pin exact tarball URL to match upstream tag naming (v2.2.0) while
    # keeping the R package Version field (2.2)
    version(
        "2.2",
        sha256="c56f104b1da1cbe91380d008dd1f16df4ed275ed81893ded983a3506ca191aa7",
        url="https://github.com/kgori/sigfit/archive/refs/tags/v2.2.0.tar.gz",
    )

    # DESCRIPTION: Depends: R (>= 3.4.0)
    depends_on("r@3.4.0:", type=("build", "run"))

    # DESCRIPTION: Imports
    depends_on("r-rcpp@0.12.0:", type=("build", "run"))
    depends_on("r-rstan@2.18.1:", type=("build", "run"))
    depends_on("r-rstantools@2.0.0:", type=("build", "run"))
    depends_on("r-coda@0.19:", type=("build", "run"))
    depends_on("r-clue@0.3:", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))

    # DESCRIPTION: LinkingTo
    depends_on("r-bh@1.66.0:", type=("build", "link", "run"))
    depends_on("r-rcppeigen@0.3.3.3.0:", type=("build", "link", "run"))
    depends_on("r-stanheaders@2.18.0:", type=("build", "link", "run"))
    # rstan is both Imported and in LinkingTo per DESCRIPTION
    depends_on("r-rstan@2.18.1:", type=("build", "link", "run"))
