# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultipanelfigure(RPackage):
    """Infrastructure to Assemble Multi-Panel Figures (from Grobs)
    
    Tools to create a layout for figures made of multiple panels, and
    to fill the panels with base, 'lattice', 'ggplot2' and 'ComplexHeatmap'
    plots, grobs, as well as content from all image formats supported by
    'ImageMagick' (accessed through 'magick').
    """

    homepage = "https://cran.r-project.org/web/packages/multipanelfigure"
    
    cran = "multipanelfigure"

    # versions
    version("2.1.2", md5="ecb6f8d11d26ac0a10191af40f86309c")
    

    # dependencies
    depends_on("r-ggplot2@2.2.1:", type=('build', 'run'))
    depends_on("r-grid", type=('build', 'run'))
    depends_on("r-gtable@0.2.0:", type=('build', 'run'))
    depends_on("r-magick@1.9:", type=('build', 'run'))
    depends_on("r-magrittr@1.5:", type=('build', 'run'))
    depends_on("r-stringi@1.2.3:", type=('build', 'run'))
    
