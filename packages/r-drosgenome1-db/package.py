# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrosgenome1Db(RPackage):
    """Affymetrix Affymetrix DrosGenome1 Array annotation data (chip drosgenome1)

    Affymetrix Affymetrix DrosGenome1 Array annotation data (chip drosgenome1) assembled using data from public repositories
    """

    bioc = "drosgenome1.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/drosgenome1.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/drosgenome1.db/drosgenome1.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="d9f2df4440466598357f05675112cc18511cd7365776d3226f0bfad2e5ab1062",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-dm-eg-db@3.13:", type=("build", "run"))
