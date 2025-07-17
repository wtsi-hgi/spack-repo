# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProstatecancercamcap(RPackage):
    """Prostate Cancer Data

    A Bioconductor data package for the Ross-Adams (2015) Prostate Cancer dataset.
    """

    bioc = "prostateCancerCamcap"

    version("1.36.0", commit="d185f4fc778bfb0cb1cfc418822f414ba53e9dc4")
    version("1.30.0", commit="235e74baa32add089c37722d41f70845f1843469")

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r@3.3:", type=("build", "run"))
