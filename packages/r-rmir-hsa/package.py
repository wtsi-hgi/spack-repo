# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmirHsa(RPackage):
    """Various databases of microRNA Targets

    Various databases of microRNA Targets
    """

    bioc = "RmiR.hsa"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/RmiR.hsa_1.0.5.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/RmiR.hsa/RmiR.hsa_1.0.5.tar.gz",
    ]

    version(
        "1.0.5",
        sha256="7f2cbbf49dcd8263335e7f8670a1c17b615c22fde02dc7d3253abf2efb1ec6b0",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
