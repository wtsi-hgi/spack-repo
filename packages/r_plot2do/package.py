# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlot2do(BundlePackage):
    """A flexible tool for evaluating the quality of MNase-seq and MNase-ChIP-seq data, and for visualizing the distribution of nucleosomes near the functional regions of the genome."""

    homepage = "https://github.com/rchereji/plot2DO"
    git = "https://github.com/rchereji/plot2DO.git"

    license("MIT")

    version("20210215", commit="2c904ab36dc27b30663b1d43ba626fb571f24f48")

    with default_args(type=("build", "run")):
        depends_on("r-colorramps")
        depends_on("r-doparallel")
        depends_on("r-foreach")
        depends_on("r-ggplot2")
        depends_on("r-gridextra")
        depends_on("r-optparse")
        depends_on("r-pracma")
        depends_on("r-reshape2")
        depends_on("r-xml2")
        depends_on("r-yaml")
        depends_on("r-annotationhub")
        depends_on("r-biomart")
        depends_on("r-genomicfeatures")
        depends_on("r-genomicranges")
        depends_on("r-genomeinfodb")
        depends_on("r-iranges")
        depends_on("r-rsamtools")
        depends_on("r-rtracklayer")
        depends_on("r-biocmanager")

    depends_on("wget")
