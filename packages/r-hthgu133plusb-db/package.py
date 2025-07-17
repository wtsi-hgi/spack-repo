# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHthgu133plusbDb(RPackage):
    """Affymetrix Affymetrix HT_HG-U133_Plus_B Array annotation data (chip hthgu133plusb)

    Affymetrix Affymetrix HT_HG-U133_Plus_B Array annotation data (chip hthgu133plusb) assembled using data from public repositories
    """

    bioc = "hthgu133plusb.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hthgu133plusb.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hthgu133plusb.db/hthgu133plusb.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="35e71809282d8276cca72468a8138abfa5e7afc61b2e13984471ae7f65d36e42",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))
