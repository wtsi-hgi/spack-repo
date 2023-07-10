# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogspline(RPackage):
    """Routines for Logspline Density Estimation
    
    Contains routines for logspline density estimation.
	The function oldlogspline() uses the same algorithm as the logspline package
	version 1.0.x; i.e. the Kooperberg and Stone (1992) 
	algorithm (with an improved interface).  The recommended routine logspline()
	uses an algorithm from Stone et al (1997)  <DOI:10.1214/aos/1031594728>.
    """

    homepage = "https://cran.r-project.org/web/packages/logspline"
    
    cran = "logspline"

    # versions
    version("2.1.20", md5="99ac414dbc76df68ff7dddbeb8f12db7")
    

    # dependencies
    depends_on("r-graphics", type=('build', 'run'))
    
