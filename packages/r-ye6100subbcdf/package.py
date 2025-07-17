# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYe6100subbcdf(RPackage):
    """ye6100subbcdf

    A package containing an environment representing the Ye6100subB.CDF file.
    """

    bioc = "ye6100subbcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ye6100subbcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ye6100subbcdf/ye6100subbcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="97d337686eb9a92f170c93b8a3156ad2df6bac2ebc649a4b482ba064ca86c984",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
