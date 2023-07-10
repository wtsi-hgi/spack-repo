# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmadaptive(RPackage):
    """Generalized Linear Mixed Models using Adaptive Gaussian
Quadrature
    
    Fits generalized linear mixed models for a single grouping factor under
    maximum likelihood approximating the integrals over the random effects with an 
    adaptive Gaussian quadrature rule; Jose C. Pinheiro and Douglas M. Bates (1995) 
    <doi:10.1080/10618600.1995.10474663>.  
    """

    homepage = "https://cran.r-project.org/web/packages/GLMMadaptive"
    
    cran = "GLMMadaptive"

    # versions
    version("0.9-0", md5="2013f505c40ded3d105da70ceeffa143")
    

    # dependencies
    depends_on("r-m-a-s-s", type=('build', 'run'))
    depends_on("r-nlme", type=('build', 'run'))
    depends_on("r-parallel", type=('build', 'run'))
    depends_on("r-matrix-stats", type=('build', 'run'))
    
