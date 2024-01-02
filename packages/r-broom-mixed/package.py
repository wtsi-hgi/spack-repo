# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RBroomMixed(RPackage):
    """Convert fitted objects from various R mixed-model packages into tidy data frames along the lines of the 'broom' package. The package provides three S3 generics for each model: tidy(), which summarizes a model's statistical findings such as coefficients of a regression; augment(), which adds columns to the original data such as predictions, residuals and cluster assignments; and glance(), which provides a one-row summary of model-level statistics."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/bbolker/broom.mixed"
    cran = "broom.mixed"

    version("0.2.9.4", sha256="7631cd29316a32050b9e72057754e053d7f9064a75900bb7e69b29ebca6c60b2")
    version("0.2.9.3", sha256="16e313f9ecd5aa5ca682454c68f96e743f153fdb5d96834a93e0e8176e608706")
    version("0.2.7", sha256="ff29385557af239a41452ffb5ebe230630a2a30f4a91e95505c3178b62df01ba")
    version("0.2.6", sha256="51ad18c65596fd3354427181a22255258738d64ef62a08c045da046ca36da8a0")
    version("0.2.5", sha256="3ec5a43b5451d422c273bf3769fadc618648b15028a9baa0b3ed1a5c90c43e88")
    version("0.2.4", sha256="4c6c3fdd89b5f473c72f11fed829955ca87d90e0546ae74f5c3d8c46e809c89c")
    version("0.2.3", sha256="798526a69eafcd014af943ca63b01e551f9ffa534979c474e1b9b0bda1e44538")
    version("0.2.2", sha256="3ea43f48a76a3b133276d06f982afecc666b12143ac571aad376d4206ca134ce")

    depends_on("r-broom", type=("build", "run"))
    depends_on("r-coda", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-nlme", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-furrr", type=("build", "run"))
