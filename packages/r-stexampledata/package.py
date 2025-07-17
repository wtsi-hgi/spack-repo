# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStexampledata(RPackage):
    """Collection of spatially-resolved transcriptomics datasets in SpatialExperiment Bioconductor format

    Collection of spatially-resolved transcriptomics (SRT) datasets in SpatialExperiment Bioconductor format, for use in examples, demonstrations, and tutorials. The datasets are from several different SRT platforms and have been sourced from various publicly available sources. Several datasets include images and/or ground truth annotation labels.
    """

    homepage = "https://github.com/lmweber/STexampleData"
    bioc = "STexampleData"

    version("1.16.0", commit="1e118c8cfa5e1c99c4fb204abf610d18fde46616")
    version("1.10.1", commit="0c643ba999034552c6ab4210054fcf2bc54e6e8e")
    version("1.10.0", md5="5fa4bfb2e58e7f6bbcd957aa1aa7e938")

    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-spatialexperiment", type=("build", "run"))
