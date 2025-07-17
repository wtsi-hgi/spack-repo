# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplots(RPackage):
    """Visualization of high-throughput assays in microtitre plate or slide format

    This package is here to support legacy usages of it, but it should not be used for new code development. It provides a single function, plotScreen, for visualising data in microtitre plate or slide format. As a better alternative for such functionality, please consider the platetools package on CRAN (https://cran.r-project.org/package=platetools and https://github.com/Swarchal/platetools), or ggplot2 (geom_raster, facet_wrap) as exemplified in the vignette of this package.
    """

    bioc = "splots"

    version("1.74.0", commit="8766bd8f4b21a77a19cc068db0bbe903466eabe4")
    version("1.68.0", commit="ab0eb02d2936637209a58142e1828ef1ce155144")

    depends_on("r-rcolorbrewer", type=("build", "run"))
