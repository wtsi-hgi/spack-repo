# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpidish(RPackage):
    """Epigenetic Dissection of Intra-Sample-Heterogeneity

    EpiDISH is a R package to infer the proportions of a priori known cell-types present in a sample representing a mixture of such cell-types. Right now, the package can be used on DNAm data of whole blood, generic epithelial tissue and breast tissue. Besides, the package provides a function that allows the identification of differentially methylated cell-types and their directionality of change in Epigenome-Wide Association Studies.
    """

    homepage = "https://github.com/sjczheng/EpiDISH"
    bioc = "EpiDISH"

    version("2.24.0", commit="9473c127d4d3aa8f877acedec8f55988cbf3e0d8")
    version("2.18.0", commit="99c055e33b433aeafd5208428b39c9163104ae12")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-quadprog", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-locfdr", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
