# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95dDb(RPackage):
    """Affymetrix Affymetrix HG_U95D Array annotation data (chip hgu95d)

    Affymetrix Affymetrix HG_U95D Array annotation data (chip hgu95d) assembled using data from public repositories
    """

    bioc = "hgu95d.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95d.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95d.db/hgu95d.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="064e22258d7059938ecbe4d94682c7e7f69d254e67c958e7d74e963bef1cf45c",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))
