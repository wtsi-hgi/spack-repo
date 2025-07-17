# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgEcsakaiEgDb(RPackage):
    """Genome wide annotation for E coli strain Sakai

    Genome wide annotation for E coli strain Sakai, primarily based on mapping using Entrez Gene identifiers.
    """

    bioc = "org.EcSakai.eg.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.EcSakai.eg.db_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.EcSakai.eg.db/org.EcSakai.eg.db_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="46bb69fce6ad5ec55fddfb1c34861d438ffcf694dc932fb5d092beb18c29860f",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
