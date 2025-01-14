# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RHdp(RPackage):
    """R pkg for Hierarchical Dirichlet Process."""

    homepage = "https://github.com/NickWilliamsSanger/hdp"
    git = "https://github.com/NickWilliamsSanger/hdp.git"

    version("0.1.5", commit="7f660c8042afc5d87c9a79be9b3e72295aa36051")

    depends_on("r-lsa", type=("build", "run"))
    depends_on("r-flexclust", type=("build", "run"))
    depends_on("r-coda", type=("build", "run"))
    depends_on("r-clue", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
