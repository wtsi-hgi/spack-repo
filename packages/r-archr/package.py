# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArchr(RPackage):
    """Analysis of Regulatory Chromatin in R."""

    homepage = "https://www.archrproject.com"
    url = "https://github.com/GreenleafLab/ArchR/archive/refs/tags/v1.0.2.tar.gz"
    git = "https://github.com/GreenleafLab/ArchR.git"

    maintainers("dorton21")

    version("1.0.3", sha256="9c07c785a095062a998ed94c65df17a58f273d0d64062c14210f0a2c491304cf")

    depends_on("r@4.0.0:", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("r-biocmanager")
        depends_on("r-devtools")
        depends_on("r-genomicranges")
        depends_on("r-summarizedexperiment")
        depends_on("r-iranges")
        depends_on("r-matrix")
        depends_on("r-rcpp")
        depends_on("r-rhdf5")
        depends_on("r-s4vectors")
        depends_on("r-data-table")
        depends_on("r-ggplot2")
        depends_on("r-plyr")
        depends_on("r-stringr")
        depends_on("r-magrittr")
        depends_on("r-pbapply")
        depends_on("r-nabor")
        depends_on("r-mass")
        depends_on("r-motifmatchr")
        depends_on("r-chromvar")
        depends_on("r-complexheatmap")
        depends_on("r-rsamtools")
        depends_on("r-biostrings")
        depends_on("r-bsgenome")
        depends_on("r-genomeinfodb")
        depends_on("r-rtracklayer")
        depends_on("r-uwot")
        depends_on("r-rann")
        depends_on("r-seurat")
        depends_on("r-biocgenerics")
        depends_on("r-monocle3")
        depends_on("r-slingshot")
        depends_on("r-presto")
        depends_on("r-harmony")
        depends_on("r-chromvarmotifs")
        depends_on("r-shiny")
        depends_on("r-shinythemes")
        depends_on("r-cairo")
        depends_on("r-ggrastr")
        depends_on("r-rhandsontable")
