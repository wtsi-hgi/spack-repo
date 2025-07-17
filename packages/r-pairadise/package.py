# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPairadise(RPackage):
    """PAIRADISE: Paired analysis of differential isoform expression

    This package implements the PAIRADISE procedure for detecting differential isoform expression between matched replicates in paired RNA-Seq data.
    """

    bioc = "PAIRADISE"

    version("1.24.1", commit="370f619f471faad39dab65ceb3f1fefc0e2f78d5")
    version("1.18.0", commit="42cef7aaa834a541de0e1a424bdb55bdff423c4a")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-nloptr", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-abind", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
