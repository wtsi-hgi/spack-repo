# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomxworkflows(RPackage):
    """GeoMx Digital Spatial Profiler (DSP) data analysis workflows

    Workflows for use with NanoString Technologies GeoMx Technology.  Package provides bioconductor focused workflows for leveraging existing packages (e.g. GeomxTools) to process, QC, and analyze the data.
    """

    bioc = "GeoMxWorkflows"

    version("1.14.0", commit="046581480b28f41f4339f423524e35d5faa14fb2")
    version("1.8.0", commit="ebedd85559c0265c52961769dbdae2228b95fb95")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-nanostringnctools", type=("build", "run"))
    depends_on("r-geomxtools", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rjson", type=("build", "run"))
    depends_on("r-readxl", type=("build", "run"))
    depends_on("r-envstats", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-outliers", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-ggforce", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-umap", type=("build", "run"))
    depends_on("r-rtsne", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
    depends_on("r-networkd3", type=("build", "run"))
