# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClariomdhumantranscriptclusterDb(RPackage):
    """Affymetrix clariomdhuman annotation data (chip clariomdhumantranscriptcluster)

    Affymetrix clariomdhuman annotation data (chip clariomdhumantranscriptcluster) assembled using data from public repositories
    """

    bioc = "clariomdhumantranscriptcluster.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/clariomdhumantranscriptcluster.db_8.8.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/clariomdhumantranscriptcluster.db/clariomdhumantranscriptcluster.db_8.8.0.tar.gz",
    ]

    version(
        "8.8.0",
        sha256="b79c7b010111999603659b4c0591a9156a9010abcc843d29be2221d94dd7cbe3",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))
