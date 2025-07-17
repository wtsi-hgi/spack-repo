# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrgepistasis(RPackage):
    """Epistasis Analysis for Quantitative Traits by Functional Regression Model

    A Tool for Epistasis Analysis Based on Functional Regression Model
    """

    bioc = "FRGEpistasis"

    version("1.44.0", commit="394010dabe707e5e7d82317381e70270f5b86998")
    version("1.38.0", commit="eada0a325aac32256b67a1e2573c9e645269978a")

    depends_on("r@2.15:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-fda", type=("build", "run"))
