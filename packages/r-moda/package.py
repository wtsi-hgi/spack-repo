# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModa(RPackage):
    """MODA: MOdule Differential Analysis for weighted gene co-expression network

    MODA can be used to estimate and construct condition-specific gene co-expression networks, and identify differentially expressed subnetworks as conserved or condition specific modules which are potentially associated with relevant biological processes.
    """

    bioc = "MODA"

    version("1.34.0", commit="e74207c80d2fec4289a20d78a29c62bf0a425cf8")
    version("1.28.0", commit="a10eb52385a191b62adee1c98c3a056fd5288ce8")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-wgcna", type=("build", "run"))
    depends_on("r-dynamictreecut", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-amountain", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
