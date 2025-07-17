# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133a2Db(RPackage):
    """Affymetrix Affymetrix HG-U133A_2 Array annotation data (chip hgu133a2)

    Affymetrix Affymetrix HG-U133A_2 Array annotation data (chip hgu133a2) assembled using data from public repositories
    """

    bioc = "hgu133a2.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133a2.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133a2.db/hgu133a2.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="1a6f84ab9d62e0aae4f6573f99d388230b77ca07eeb26eaab59f54c7a171b272",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))
