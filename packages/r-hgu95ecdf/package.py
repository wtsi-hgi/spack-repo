# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95ecdf(RPackage):
    """hgu95ecdf

    A package containing an environment representing the HG_U95E.CDF file.
    """

    bioc = "hgu95ecdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95ecdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95ecdf/hgu95ecdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="3baf7002d77566e4c59ae1ee73d15ce887b2a5a1e58b1870186cd80ed73ec90b",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
