# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoplarcdf(RPackage):
    """poplarcdf

    A package containing an environment representing the Poplar.cdf file.
    """

    bioc = "poplarcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/poplarcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/poplarcdf/poplarcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="81be005908e4f039fb9708e5787a66d4315903e50b0f73f9e3429a91f4674848",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
