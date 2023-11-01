# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRootsolve(RPackage):
    """Routines to find the root of nonlinear functions, and to perform steady-state and equilibrium analysis of ordinary differential equations"""

    homepage = "https://cran.r-project.org/web/packages/rootSolve/index.html"

    cran = "rootSolve"
    version("1.8.2.4", sha256="e16a317ea494192e0a5668a18f7eb99675f8edf3b3095861d213bc2590ad385d")

    depends_on("r+X", type=("build", "run"))

