# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfess(RPackage):
    """Cell OrderiNg by FluorEScence Signal

    Single Cell Fluidigm Spot Detector.
    """

    bioc = "CONFESS"

    version("1.36.0", commit="eccc13f5862b00a16f1f4ccee84cbf8e963866b6")
    version("1.30.0", commit="641088d81bf1a040b91c2c6c0693bdb4f3411874")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-changepoint", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-contrast", type=("build", "run"))
    depends_on("r-data-table@1.9.7:", type=("build", "run"))
    depends_on("r-ecp", type=("build", "run"))
    depends_on("r-ebimage", type=("build", "run"))
    depends_on("r-flexmix", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-flowclust", type=("build", "run"))
    depends_on("r-flowmeans", type=("build", "run"))
    depends_on("r-flowmerge", type=("build", "run"))
    depends_on("r-flowpeaks", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-moments", type=("build", "run"))
    depends_on("r-outliers", type=("build", "run"))
    depends_on("r-plotrix", type=("build", "run"))
    depends_on("r-raster", type=("build", "run"))
    depends_on("r-readbitmap", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-samspectral", type=("build", "run"))
    depends_on("r-waveslim", type=("build", "run"))
    depends_on("r-wavethresh", type=("build", "run"))
    depends_on("r-zoo", type=("build", "run"))
