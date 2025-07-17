# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZebrafishDb(RPackage):
    """Affymetrix Affymetrix Zebrafish Array annotation data (chip zebrafish)

    Affymetrix Affymetrix Zebrafish Array annotation data (chip zebrafish) assembled using data from public repositories
    """

    bioc = "zebrafish.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/zebrafish.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/zebrafish.db/zebrafish.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="87c11e062cf3a519426bf861ab18090f088cd304b905289093b8e491bb2c468d",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-dr-eg-db@3.13:", type=("build", "run"))
