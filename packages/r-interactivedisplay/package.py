# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInteractivedisplay(RPackage):
    """Package for enabling powerful shiny web displays of Bioconductor objects

    The interactiveDisplay package contains the methods needed to generate interactive Shiny based display methods for Bioconductor objects.
    """

    bioc = "interactiveDisplay"
    urls = [
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/interactiveDisplay_1.40.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/interactiveDisplay/interactiveDisplay_1.40.0.tar.gz",
    ]

    version("1.40.0", sha256="2a3e31639245081cd69f4c0c6396231a39b5477eda8362e956f221c266610171")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-interactivedisplaybase@1.7.3:", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-gridsvg", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-category", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))

    def patch(self):
        for i in ['if (!requireNamespace("BiocManager", quietly=TRUE))', 'install.packages("BiocManager")']:
            filter_file(i, "", "R/interactiveDisplay.R", string=True)
