# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REditdata(RPackage):
    """'RStudio' Addin for Editing a 'data.frame'
    
    An 'RStudio' addin for editing a 'data.frame' or a 'tibble'. You can delete, add or update a 'data.frame'
    without coding. You can get resultant data as a 'data.frame'. In the package, modularized 'shiny' app codes are provided. 
    These modules are intended for reuse across applications.
    """

    homepage = "https://cran.r-project.org/web/packages/editData"
    
    cran = "editData"

    # versions
    version("0.1.8", md5="dd6b1d8617798734fc33cfb42e69173c")
    

    # dependencies
    depends_on("r@2.10:", type=('build', 'run'))
    depends_on("r-shiny@0.13:", type=('build', 'run'))
    depends_on("r-mini-u-i@0.1.1:", type=('build', 'run'))
    depends_on("r-rstudioapi@0.5:", type=('build', 'run'))
    depends_on("r-tibble", type=('build', 'run'))
    depends_on("r-dplyr", type=('build', 'run'))
    depends_on("r-rio", type=('build', 'run'))
    depends_on("r-magrittr", type=('build', 'run'))
    depends_on("r-shiny-widgets", type=('build', 'run'))
    depends_on("r-openxlsx", type=('build', 'run'))
    
