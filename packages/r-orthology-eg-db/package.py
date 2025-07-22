# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrthologyEgDb(RPackage):
    """Orthology mapping package

    Orthology mapping package, based on data from NCBI, using NCBI Gene IDs and Taxonomy IDs.
    """

    bioc = "Orthology.eg.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Orthology.eg.db_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/Orthology.eg.db/Orthology.eg.db_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="f2b3b214d8a9d4bc3352cab1ad8e9e5c119506bac582331316a30e4044756687",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
