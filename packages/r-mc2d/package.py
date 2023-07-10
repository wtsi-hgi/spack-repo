# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMc2d(RPackage):
    """Tools for Two-Dimensional Monte-Carlo Simulations
    
    A complete framework to build and study Two-Dimensional Monte-Carlo simulations, aka Second-Order Monte-Carlo simulations. Also includes various distributions (pert, triangular, Bernoulli, empirical discrete and continuous).
    """

    homepage = "https://cran.r-project.org/web/packages/mc2d"
    
    cran = "mc2d"

    # versions
    version("0.1-22", md5="9e03eba5b8b6abe0728c58299800dd0e")
    

    # dependencies
    depends_on("r-gr-devices", type=('build', 'run'))
    depends_on("r-graphics", type=('build', 'run'))
    
