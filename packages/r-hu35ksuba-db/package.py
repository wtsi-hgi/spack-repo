# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubaDb(RPackage):
    """Affymetrix Affymetrix Hu35KsubA Array annotation data (chip hu35ksuba)

    Affymetrix Affymetrix Hu35KsubA Array annotation data (chip hu35ksuba) assembled using data from public repositories
    """

    bioc = "hu35ksuba.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu35ksuba.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu35ksuba.db/hu35ksuba.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="8319194bee8cd7a939fb2423e81126bd74970373ea3a9803a2addc7d0f4b4f48",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))
