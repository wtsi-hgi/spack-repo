# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu219cdf(RPackage):
    """hgu219cdf

    A package containing an environment representing the HG-U219.cdf file.
    """

    bioc = "hgu219cdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu219cdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu219cdf/hgu219cdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="0d7c4b57ab3de6a70e6fa20687496d958c47ffd1ee22dab5dee44282f2b16b92",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
