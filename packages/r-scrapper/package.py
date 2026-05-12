# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrapper(RPackage):
    """Bindings to C++ libraries for single cell analysis.

    Provides R wrappers around the libscran C++ utilities that power a number
    of single-cell workflows, covering functionality such as quality control,
    normalization, clustering, and marker detection."""

    homepage = "https://bioconductor.org/packages/release/bioc/html/scrapper.html"
    bioc = "scrapper"
    git = "https://git.bioconductor.org/packages/scrapper"

    license("MIT")

    version("1.4.0", tag="RELEASE_3_22")

    depends_on("r@4.4:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-beachmat@2.25.1:", type=("build", "run"))
    depends_on("r-delayedarray@0.27.2:", type=("build", "run"))
    depends_on("r-biocneighbors@1.99.0:", type=("build", "run"))
    depends_on("r-rigraphlib@1.2.0", type=("build", "run"))
    depends_on("r-assorthead@1.3.10:", type=("build", "run"))

    # Suggests
    depends_on("r-knitr", type=("build"))
    depends_on("r-rmarkdown", type=("build"))
    depends_on("r-biocstyle", type=("build"))
    depends_on("r-testthat", type=("build"))
