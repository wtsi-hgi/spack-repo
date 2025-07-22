# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellhts2(RPackage):
    """Analysis of cell-based screens - revised version of cellHTS

    This package provides tools for the analysis of high-throughput assays that were performed in microtitre plate formats (including but not limited to 384-well plates). The functionality includes data import and management, normalisation, quality assessment, replicate summarisation and statistical scoring. A webpage that provides a detailed graphical overview over the data and analysis results is produced. In our work, we have applied the package to RNAi screens on fly and human cells, and for screens of yeast libraries. See ?cellHTS2 for a brief introduction.
    """

    homepage = "http://www.dkfz.de/signaling"
    bioc = "cellHTS2"

    version("2.66.0", commit="3fe8e7d83a448c4d8df27447ac581268ba577d85")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-genefilter", type=("build", "run"))
    depends_on("r-splots", type=("build", "run"))
    depends_on("r-vsn", type=("build", "run"))
    depends_on("r-hwriter", type=("build", "run"))
    depends_on("r-locfit", type=("build", "run"))
    depends_on("r-gseabase", type=("build", "run"))
    depends_on("r-category", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
