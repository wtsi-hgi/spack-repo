# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClariomsmousetranscriptclusterDb(RPackage):
    """Affymetrix clariomsmouse annotation data (chip clariomsmousetranscriptcluster)

    Affymetrix clariomsmouse annotation data (chip clariomsmousetranscriptcluster) assembled using data from public repositories
    """

    bioc = "clariomsmousetranscriptcluster.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/clariomsmousetranscriptcluster.db_8.8.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/clariomsmousetranscriptcluster.db/clariomsmousetranscriptcluster.db_8.8.0.tar.gz",
    ]

    version(
        "8.8.0",
        sha256="6ce5f4d70cf5ab3443947e37afdf40aafb029285f01cfde0dda6ac9a8d96cb84",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))
