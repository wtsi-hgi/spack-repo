# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95av2cdf(RPackage):
    """hgu95av2cdf

    A package containing an environment representing the HG_U95Av2.CDF file.
    """

    bioc = "hgu95av2cdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95av2cdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95av2cdf/hgu95av2cdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="d449a06a2f55a5a1f942710c8da2a37a81e20342b6e600669df94ecb55f1e1fe",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
