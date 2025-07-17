# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClariomsrattranscriptclusterDb(RPackage):
    """Affymetrix clariomsrat annotation data (chip clariomsrattranscriptcluster)

    Affymetrix clariomsrat annotation data (chip clariomsrattranscriptcluster) assembled using data from public repositories
    """

    bioc = "clariomsrattranscriptcluster.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/clariomsrattranscriptcluster.db_8.8.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/clariomsrattranscriptcluster.db/clariomsrattranscriptcluster.db_8.8.0.tar.gz",
    ]

    version(
        "8.8.0",
        sha256="1ee628b259daa83c83bcee168302df406e80947cbfb0881e71158148494d6d44",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))
