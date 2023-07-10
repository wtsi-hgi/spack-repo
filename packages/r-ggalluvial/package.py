# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgalluvial(RPackage):
    """Alluvial Plots in 'ggplot2'
    
    Alluvial plots use variable-width ribbons and stacked bar plots to
    represent multi-dimensional or repeated-measures data with categorical or
    ordinal variables; see Riehmann, Hanfler, and Froehlich (2005)
    <doi:10.1109/INFVIS.2005.1532152> and Rosvall and Bergstrom (2010)
    <doi:10.1371/journal.pone.0008694>.
    Alluvial plots are statistical graphics in the sense of Wilkinson (2006)
    <doi:10.1007/0-387-28695-0>; they share elements with Sankey diagrams and
    parallel sets plots but are uniquely determined from the data and a small
    set of parameters. This package extends Wickham's (2010)
    <doi:10.1198/jcgs.2009.07098> layered grammar of graphics to generate
    alluvial plots from tidy data.
    """

    homepage = "https://cran.r-project.org/web/packages/ggalluvial"
    
    cran = "ggalluvial"

    # versions
    version("0.12.5", md5="fa28d48c3a3b6f8c8a61ee6436204e27")
    

    # dependencies
    depends_on("r-dplyr@0.7:", type=('build', 'run'))
    depends_on("r-tidyr@0.7:", type=('build', 'run'))
    depends_on("r-lazyeval", type=('build', 'run'))
    depends_on("r-rlang", type=('build', 'run'))
    depends_on("r-tidyselect", type=('build', 'run'))
    
