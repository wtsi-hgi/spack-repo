# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinybs(RPackage):
    """Twitter Bootstrap Components for Shiny
    
    Adds additional Twitter Bootstrap components to Shiny. 
    """

    homepage = "https://cran.r-project.org/web/packages/shinyBS"
    
    cran = "shinyBS"

    # versions
    version("0.61.1", md5="906917fce92a851081f5755340d2bea0")
    

    # dependencies
    depends_on("r-shiny@0.11:", type=('build', 'run'))
    depends_on("r-htmltools", type=('build', 'run'))
    
