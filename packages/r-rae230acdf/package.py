# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRae230acdf(RPackage):
    """rae230acdf

    A package containing an environment representing the RAE230A.CDF file.
    """

    bioc = "rae230acdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rae230acdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rae230acdf/rae230acdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="130988dbd2256f88a75afdf794dc3895b45faafe6a0e8635a9b9c28a027fc2b8",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
