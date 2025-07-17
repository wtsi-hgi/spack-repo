# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95acdf(RPackage):
    """hgu95acdf

    A package containing an environment representing the HG_U95A.CDF file.
    """

    bioc = "hgu95acdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95acdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95acdf/hgu95acdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="d94e1eba151113248d25255bd3ed59039b4382048e9e32d01cf66fd07661aad7",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
