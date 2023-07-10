# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinywidgets(RPackage):
    """Custom Inputs Widgets for Shiny
    
    Collection of custom input controls and user interface components for 'Shiny' applications. 
  Give your applications a unique and colorful style !
    """

    homepage = "https://cran.r-project.org/web/packages/shinyWidgets"
    
    cran = "shinyWidgets"

    # versions
    version("0.7.6", md5="b384f520497179381d14b5a5e565529b")
    

    # dependencies
    depends_on("r@3.1.0:", type=('build', 'run'))
    depends_on("r-anytime", type=('build', 'run'))
    depends_on("r-bslib", type=('build', 'run'))
    depends_on("r-sass", type=('build', 'run'))
    depends_on("r-shiny@1.6.0:", type=('build', 'run'))
    depends_on("r-htmltools@0.5.1:", type=('build', 'run'))
    depends_on("r-jsonlite", type=('build', 'run'))
    depends_on("r-gr-devices", type=('build', 'run'))
    depends_on("r-rlang", type=('build', 'run'))
    
