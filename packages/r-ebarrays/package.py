# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbarrays(RPackage):
    """Unified Approach for Simultaneous Gene Clustering and Differential Expression Identification

    EBarrays provides tools for the analysis of replicated/unreplicated microarray data.
    """

    bioc = "EBarrays"

    version("2.72.0", commit="cb4b847b9b683a9ce88ee3fae29e6727b9ab1ff0")
    version("2.66.0", commit="8f2e6be7b512d374449bb187c5ec86922eb5a920")

    depends_on("r@1.8:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
