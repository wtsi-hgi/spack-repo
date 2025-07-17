# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElmer(RPackage):
    """Inferring Regulatory Element Landscapes and Transcription Factor Networks Using Cancer Methylomes

    ELMER is designed to use DNA methylation and gene expression from a large number of samples to infere regulatory element landscape and transcription factor network in primary tissue.
    """

    bioc = "ELMER"

    version("2.32.0", commit="b1c7e3b8ca491cab5d9597f2e88ea37c6d4ddafc")
    version("2.26.0", commit="ceacb6a96053e969b690c811b042707317d38c65")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-elmer-data@2.9.3:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-tcgabiolinks@2.23.7:", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-downloader", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-rvest", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-progress", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-ggpubr", type=("build", "run"))
    depends_on("r-rtracklayer@1.61.2:", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
