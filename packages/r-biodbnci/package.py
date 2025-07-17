# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodbnci(RPackage):
    """biodbNci, a library for connecting to biodbNci, a library for connecting to the National Cancer Institute (USA) CACTUS Database

    The biodbNci library is an extension of the biodb framework package. It provides access to biodbNci, a library for connecting to the National Cancer Institute (USA) CACTUS Database. It allows to retrieve entries by their accession number, and run specific web services.
    """

    bioc = "biodbNci"

    version("1.12.0", commit="a398ae4d2114807429fd88d8d59070fc3dbb2eb9")
    version("1.6.0", commit="f5993f44971be1e4791d1d087c307f82764046c4")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-biodb@1.3.1:", type=("build", "run"))
    depends_on("r-r6", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-chk", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
