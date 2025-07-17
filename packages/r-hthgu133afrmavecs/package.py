# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHthgu133afrmavecs(RPackage):
    """Vectors used by frma for microarrays of type hthgu133a

    This package was created by frmaTools version 1.19.3 and hgu133ahsentrezgcdf version 19.0.0.
    """

    bioc = "hthgu133afrmavecs"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hthgu133afrmavecs_1.3.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hthgu133afrmavecs/hthgu133afrmavecs_1.3.0.tar.gz",
    ]

    version(
        "1.3.0",
        sha256="5a13bb2e2229418d9649b4bc8050437d6f931958d100cdcebdb9e463e2ebc610",
    )

    depends_on("r@2.10:", type=("build", "run"))
