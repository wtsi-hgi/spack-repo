# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColliderbias(RPackage):
    """This is the R package for CWLS (Corrected Weighted Least Squares) and CWBLS (Corrected Weighted Bivariate Least Squares), a designed method to adjust for collider bias in Mendelian Randomisation using summary statistics from GWAS studies."""

    homepage = "https://github.com/SiyangCai/ColliderBias"
    git = "https://github.com/SiyangCai/ColliderBias.git"

    version("2024.11.01", commit="66606d074c5cfd5263a0e2234ceb0a88fc9fdbc1")

    depends_on("r-boot", type=("build", "run"))
    depends_on("r-mr-raps", type=("build", "run"))
    depends_on("r-slopehunter", type=("build", "run"))
