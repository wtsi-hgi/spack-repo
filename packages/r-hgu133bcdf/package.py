# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133bcdf(RPackage):
    """hgu133bcdf

    A package containing an environment representing the HG-U133B.cdf file.
    """

    bioc = "hgu133bcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133bcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133bcdf/hgu133bcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="637fbe6bbf4cf515c961264e69c3b820f3d7b3cf8a127010718e95e16e218f36",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
