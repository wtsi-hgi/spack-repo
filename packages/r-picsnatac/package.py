# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPicsnatac(RPackage):
    """Paired insertion counting workflows for single-nucleus ATAC-seq data."""

    homepage = "https://github.com/Zhen-Miao/PICsnATAC"
    url = "https://github.com/Zhen-Miao/PICsnATAC/archive/refs/tags/v0.3.1.tar.gz"
    git = "https://github.com/Zhen-Miao/PICsnATAC.git"

    license("MIT")

    version("0.3.1", sha256="4a75d4cf5f969a0f5065d14def903ddbcf68de6925673bbff5698a352305d1cc")
    version("0.3.0", sha256="46f0d176ad871db0e2ae0b9b39c7a4339a16a68cfd8b8110f1f4aa9bb61864c1")
    version("0.2.3", sha256="325342a693498b74557dd25cc71760c1ea4a33d6a8bfa158b5e1badda455f3f2")
    version("0.2.2", sha256="3a821e56865ad1718ff75e351b74ae891c0fd7a74afdf2b3e10d4ca122a18c47")

    depends_on("r@4.0.0:", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("r-genomicranges")
        depends_on("r-iranges")
        depends_on("r-matrix")
        depends_on("r-data-table")
        depends_on("r-rsamtools")
        depends_on("r-genomeinfodb")
        depends_on("r-tidyr")
        depends_on("r-progress")
