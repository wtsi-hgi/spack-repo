# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133acdf(RPackage):
    """hgu133acdf

    A package containing an environment representing the HG-U133A.cdf file.
    """

    bioc = "hgu133acdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133acdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133acdf/hgu133acdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="865964787e1ce061f3ff03c8ae0ee3fbeb8f9cd0a6fc2ccb34625d48fe064a81",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
