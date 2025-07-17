# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProstatecancerstockholm(RPackage):
    """Prostate Cancer Data

    A Bioconductor data package for the Stockholm dataset
    """

    bioc = "prostateCancerStockholm"

    version("1.36.0", commit="c6c3cd54c8a633d332a15665d12cc91ec7337309")
    version("1.30.0", commit="ab4142f874cacfb155d9f63a4cd9a56f3514f893")

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r@3.3:", type=("build", "run"))
