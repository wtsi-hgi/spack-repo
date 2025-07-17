# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNnnorm(RPackage):
    """Spatial and intensity based normalization of cDNA microarray data based on robust neural nets

    This package allows to detect and correct for spatial and intensity biases with two-channel microarray data. The normalization method implemented in this package is based on robust neural networks fitting.
    """

    homepage = "http://bioinformaticsprb.med.wayne.edu/tarca/"
    bioc = "nnNorm"

    version("2.72.0", commit="d9432ed56fc448bb39f4c228f8c25812ffafc718")
    version("2.66.0", commit="cdf849728c646e9b4e8f5a31d7b7fa6d51d0aff7")

    depends_on("r@2.2:", type=("build", "run"))
    depends_on("r-marray", type=("build", "run"))
    depends_on("r-nnet", type=("build", "run"))
