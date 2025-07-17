# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSampleclassifierdata(RPackage):
    """Pre-processed data for use with the sampleClassifier package

    This package contains two microarray and two RNA-seq datasets that have been preprocessed for use with the sampleClassifier package. The RNA-seq data are derived from Fagerberg et al. (2014) and the Illumina Body Map 2.0 data. The microarray data are derived from Roth et al. (2006) and Ge et al. (2005).
    """

    bioc = "sampleClassifierData"

    version("1.32.0", commit="d2d5aad9d0e28703ec97b3a8085e993a3fcb6cd0")
    version("1.26.0", commit="06af2100ac79462d6111b42cf8b91f8d334a1e69")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
