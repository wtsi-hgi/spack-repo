# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrench(RPackage):
    """Wrench normalization for sparse count data

    Wrench is a package for normalization sparse genomic count data, like that arising from 16s metagenomic surveys.
    """

    homepage = "https://github.com/HCBravoLab/Wrench"
    bioc = "Wrench"

    version("1.26.0", commit="369d5b183ca7a5f58c654b0ef492e10eb3d91cd5")
    version("1.20.0", commit="b8512e20b95e3ce2c85fa473e0fb334572fbae4b")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-locfit", type=("build", "run"))
