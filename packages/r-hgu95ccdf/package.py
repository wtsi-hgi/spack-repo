# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95ccdf(RPackage):
    """hgu95ccdf

    A package containing an environment representing the HG_U95C.CDF file.
    """

    bioc = "hgu95ccdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95ccdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95ccdf/hgu95ccdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="2d0f1b7ad5873c57470e9074f6c074db12d1d962b4b5cd6c8ee3f11a101551d5",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
