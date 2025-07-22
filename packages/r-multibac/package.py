# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultibac(RPackage):
    """Multiomic Batch effect Correction

    MultiBaC is a strategy to correct batch effects from multiomic datasets distributed across different labs or data acquisition events. MultiBaC is the first Batch effect correction algorithm that dealing with batch effect correction in multiomics datasets. MultiBaC is able to remove batch effects across different omics generated within separate batches provided that at least one common omic data type is included in all the batches considered.
    """

    bioc = "MultiBaC"

    version("1.18.0", commit="aeda3f880c86f22b9892c9520e82ebabcf2bbdf3")
    version("1.12.0", commit="63372e330ce0aa77054ab6124fc7871b8020d737")

    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-ropls", type=("build", "run"))
    depends_on("r-plotrix", type=("build", "run"))
    depends_on("r-pcamethods", type=("build", "run"))
