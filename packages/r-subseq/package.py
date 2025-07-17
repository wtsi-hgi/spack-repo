# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubseq(RPackage):
    """Subsampling of high-throughput sequencing count data

    Subsampling of high throughput sequencing count data for use in experiment design and analysis.
    """

    homepage = "http://github.com/StoreyLab/subSeq"
    bioc = "subSeq"

    version("1.38.0", commit="e7d552794fd72a4310d5fd1e4ff221d152c8d246")
    version("1.32.0", commit="ada9c5be8d3068e1de56eeaf4132c204cdc1e9e1")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-qvalue@1.99:", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
