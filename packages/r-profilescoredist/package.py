# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfilescoredist(RPackage):
    """Profile score distributions

    Regularization and score distributions for position count matrices.
    """

    bioc = "profileScoreDist"

    version("1.36.0", commit="4ad0ca770bbf18e58e1db1007a47f2bdc2747d19")
    version("1.30.0", commit="d8bfff1199ba20c2d98806c8292288784cae9b0b")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
