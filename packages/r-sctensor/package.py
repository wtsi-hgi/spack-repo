# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSctensor(RPackage):
    """Detection of cell-cell interaction from single-cell RNA-seq dataset by tensor decomposition

    The algorithm is based on the non-negative tucker decomposition (NTD2) of nnTensor.
    """

    bioc = "scTensor"

    version("2.18.2", commit="3d3fb3920b973ae4e7c35bbad05fd3b43ce130c0")
    version("2.12.0", commit="40a43b37a498476e26d21f0c921d4289288538fd")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-reactome-db", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-nntensor@1.1.5:", type=("build", "run"))
    depends_on("r-cctensor@1.0.2:", type=("build", "run"))
    depends_on("r-rtensor@1.4.8:", type=("build", "run"))
    depends_on("r-abind", type=("build", "run"))
    depends_on("r-plotrix", type=("build", "run"))
    depends_on("r-heatmaply", type=("build", "run"))
    depends_on("r-tagcloud", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-meshdbi@1.29.2:", type=("build", "run"))
    depends_on("r-outliers", type=("build", "run"))
    depends_on("r-category", type=("build", "run"))
    depends_on("r-meshr@1.99.1:", type=("build", "run"))
    depends_on("r-gostats", type=("build", "run"))
    depends_on("r-reactomepa", type=("build", "run"))
    depends_on("r-dose", type=("build", "run"))
    depends_on("r-crayon", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
    depends_on("r-visnetwork", type=("build", "run"))
    depends_on("r-schex", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
