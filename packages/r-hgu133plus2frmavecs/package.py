# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133plus2frmavecs(RPackage):
    """Vectors used by frma for microarrays of type hgu133plus2

    This package was created by frmaTools version 1.19.3 and hgu133ahsentrezgcdf version 19.0.0.
    """

    bioc = "hgu133plus2frmavecs"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133plus2frmavecs_1.5.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133plus2frmavecs/hgu133plus2frmavecs_1.5.0.tar.gz",
    ]

    version(
        "1.5.0",
        sha256="0c1053763530e22741bdc68846daac86b48913d56b8c3e490174d4de31246fe4",
    )

    depends_on("r@2.10:", type=("build", "run"))
