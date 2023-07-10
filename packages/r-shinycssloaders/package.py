# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinycssloaders(RPackage):
    """Add Loading Animations to a 'shiny' Output While It's
Recalculating
    
    When a 'Shiny' output (such as a plot, table, map, etc.) is recalculating, it remains 
    visible but gets greyed out. Using 'shinycssloaders', you can add a loading animation ("spinner")
    to outputs instead. By wrapping a 'Shiny' output in 'withSpinner()', a spinner will automatically
    appear while the output is recalculating. See the demo online at
    <https://daattali.com/shiny/shinycssloaders-demo/>.
    """

    homepage = "https://cran.r-project.org/web/packages/shinycssloaders"
    
    cran = "shinycssloaders"

    # versions
    version("1.0.0", md5="2a78821ff0c15044e1388d2bbe7dfbe1")
    

    # dependencies
    depends_on("r@3.1:", type=('build', 'run'))
    depends_on("r-digest", type=('build', 'run'))
    depends_on("r-glue", type=('build', 'run'))
    depends_on("r-gr-devices", type=('build', 'run'))
    depends_on("r-shiny", type=('build', 'run'))
    
