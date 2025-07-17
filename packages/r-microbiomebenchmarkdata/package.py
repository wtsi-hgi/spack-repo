# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobiomebenchmarkdata(RPackage):
    """Datasets for benchmarking in microbiome research

    The MicrobiomeBenchmarkData package provides functionality to access microbiome datasets suitable for benchmarking. These datasets have some biological truth, which allows to have expected results for comparison. The datasets come from various published sources and are provided as TreeSummarizedExperiment objects. Currently, only datasets suitable for benchmarking differential abundance methods are available.
    """

    homepage = "https://github.com/waldronlab/MicrobiomeBenchmarkData"
    bioc = "MicrobiomeBenchmarkData"

    version("1.10.0", commit="615e0573eaed0918fd2fa75ef5921556243ae0c7")
    version("1.4.0", commit="a9465e2e68e8c01fc042ae0231498dbdce7337b5")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-treesummarizedexperiment", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
