# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRat2302cdf(RPackage):
    """rat2302cdf

    A package containing an environment representing the Rat230_2.cdf file.
    """

    bioc = "rat2302cdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rat2302cdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rat2302cdf/rat2302cdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="93270f296d8f2ee8c81fcb7cd9a703bd6b76c5300f87fc38f2a75def0dcb889c",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
