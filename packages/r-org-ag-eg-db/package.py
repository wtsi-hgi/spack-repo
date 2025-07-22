# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgAgEgDb(RPackage):
    """Genome wide annotation for Anopheles

    Genome wide annotation for Anopheles, primarily based on mapping using Entrez Gene identifiers.
    """

    bioc = "org.Ag.eg.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Ag.eg.db_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Ag.eg.db/org.Ag.eg.db_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="9ffa0f60cf6788628c152b7840f0cc24687076972082ab1b1f62ecebd1ef2bc9",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
