# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPicsnatac(RPackage):
    """Paired insertion counting for snATAC-seq data."""

    homepage = "https://github.com/Zhen-Miao/PICsnATAC"
    url = "https://github.com/Zhen-Miao/PICsnATAC/archive/refs/tags/v0.3.1.tar.gz"
    git = "https://github.com/Zhen-Miao/PICsnATAC.git"

    version("0.3.1", sha256="4a75d4cf5f969a0f5065d14def903ddbcf68de6925673bbff5698a352305d1cc")
    version("0.3.0", sha256="46f0d176ad871db0e2ae0b9b39c7a4339a16a68cfd8b8110f1f4aa9bb61864c1")

    depends_on("r@4.0.0:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-progress", type=("build", "run"))
