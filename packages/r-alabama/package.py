# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabama(RPackage):
    """Constrained Nonlinear Optimization
    
    Augmented Lagrangian Adaptive Barrier Minimization
        Algorithm for optimizing smooth nonlinear objective functions
        with constraints. Linear or nonlinear equality and inequality
        constraints are allowed.
    """

    homepage = "https://cran.r-project.org/web/packages/alabama"
    
    cran = "alabama"

    # versions
    version("2022.4-1", md5="92bde73c545c27b2fa781d8b5e4378dd")
    

    # dependencies
    
