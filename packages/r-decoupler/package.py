# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecoupler(RPackage):
    """Ensemble methods to infer biological activities from omics data."""

    homepage = "https://bioconductor.org/packages/release/bioc/html/decoupleR.html"
    bioc = "decoupleR"

    version(
        "2.9.7",
        sha256="a4adc855862b31268fbff9f7a3e5e13ec9ad416cc17dd43a5d72c46492fddb5d",
        url="https://github.com/saezlab/decoupleR/archive/refs/tags/v2.9.7.tar.gz",
    )
    version(
        "2.8.0",
        sha256="09b6d3398eec6e5aa6eacd41c8d025488e6acc771e04e43040cb8ea1feccd4ee",
        url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/decoupleR_2.8.0.tar.gz",
    )

    depends_on("r@4.0:", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("r-biocparallel")
        depends_on("r-broom")
        depends_on("r-dplyr")
        depends_on("r-magrittr")
        depends_on("r-matrix")
        depends_on("r-parallelly")
        depends_on("r-purrr")
        depends_on("r-rlang")
        depends_on("r-stringr")
        depends_on("r-tibble")
        depends_on("r-tidyr")
        depends_on("r-tidyselect")
        depends_on("r-withr")
