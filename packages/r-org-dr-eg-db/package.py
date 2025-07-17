# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgDrEgDb(RPackage):
    """Genome wide annotation for Zebrafish

    Genome wide annotation for Zebrafish, primarily based on mapping using Entrez Gene identifiers.
    """

    bioc = "org.Dr.eg.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Dr.eg.db_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Dr.eg.db/org.Dr.eg.db_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="ec9ba29db1ec0733a953f52c376a8e33a70c31d7fd56728be30f62f6d79365ce",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
