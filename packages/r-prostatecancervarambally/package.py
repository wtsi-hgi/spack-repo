# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProstatecancervarambally(RPackage):
    """Prostate Cancer Data

    A Bioconductor data package for the Varambally dataset
    """

    bioc = "prostateCancerVarambally"

    version("1.36.0", commit="73f630d7e7602f9a26191b44a4d79ef8bc248ce5")
    version("1.30.0", commit="3c16ae46c24c5c2b493deda60c0a8a30a6c3b1d5")

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r@3.3:", type=("build", "run"))
