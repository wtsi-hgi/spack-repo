# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgspavis(RPackage):
    """Visualization functions for spatially resolved transcriptomics data

    Visualization functions for spatially resolved transcriptomics datasets stored in SpatialExperiment format. Includes functions to create several types of plots for data from from spot-based (e.g. 10x Genomics Visium) and molecule-based (e.g. seqFISH) technological platforms.
    """

    homepage = "https://github.com/lmweber/ggspavis"
    bioc = "ggspavis"

    version("1.14.3", commit="2aef401710ebd98a5b5a35b1768d7a7e82dece5d")
    version("1.8.1", commit="c036da7f38d7093c5df8b8f8d7ff0d65386223ab")
    version("1.8.0", md5="c79337783dc059e449506a61c5579337")

    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-spatialexperiment", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-ggside", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
