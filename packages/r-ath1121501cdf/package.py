# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAth1121501cdf(RPackage):
    """ath1121501cdf

    A package containing an environment representing the ATH1-121501.CDF file.
    """

    bioc = "ath1121501cdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ath1121501cdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ath1121501cdf/ath1121501cdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="8ce15cf422d4ba285d238b070ebaa4a54b68f815d5a2137ab3753dde904358d9",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
