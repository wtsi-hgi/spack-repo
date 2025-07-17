# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestfulsedata(RPackage):
    """Example metadata for the "restfulSE" R package

    Metadata RangedSummarizedExperiment shell for use with restfulSE.
    """

    bioc = "restfulSEData"

    version("1.24.0", commit="2e6df54780ea3331a7a41b39c2284a3c6982564a")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-delayedarray@0.21.2:", type=("build", "run"))
    depends_on("r-hdf5array@1.23.2:", type=("build", "run"))
