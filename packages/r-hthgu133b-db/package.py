# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHthgu133bDb(RPackage):
    """Affymetrix Affymetrix HT_HG-U133B Array annotation data (chip hthgu133b)

    Affymetrix Affymetrix HT_HG-U133B Array annotation data (chip hthgu133b) assembled using data from public repositories
    """

    bioc = "hthgu133b.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hthgu133b.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hthgu133b.db/hthgu133b.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="2ddfa6edff4416154d6b120574c50bc0395dabdd6e81885ed70750367f684a30",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))
