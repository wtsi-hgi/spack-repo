# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmg430aDb(RPackage):
    """Affymetrix Affymetrix HT_MG-430A Array annotation data (chip htmg430a)

    Affymetrix Affymetrix HT_MG-430A Array annotation data (chip htmg430a) assembled using data from public repositories
    """

    bioc = "htmg430a.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htmg430a.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htmg430a.db/htmg430a.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="d2d6e94fdff89640eca79f41e8eb8814fa9230a178e9a774d3d0d7303fbd4a53",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))
