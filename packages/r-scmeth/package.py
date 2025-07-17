# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScmeth(RPackage):
    """Functions to conduct quality control analysis in methylation data

    Functions to analyze methylation data can be found here. Some functions are relevant for single cell methylation data but most other functions can be used for any methylation data. Highlight of this workflow is the comprehensive quality control report.
    """

    bioc = "scmeth"

    version("1.28.0", commit="3d3725996adb7948e3523ec007cc25cbd578b0e8")
    version("1.22.0", commit="39a201a9a80b01c87bf294ebc088a869b8e8654e")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-bsseq", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-delayedarray@0.5.15:", type=("build", "run"))
    depends_on("r-annotatr", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.5.6:", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-hdf5array@1.7.5:", type=("build", "run"))
