# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgSsEgDb(RPackage):
    """Genome wide annotation for Pig

    Genome wide annotation for Pig, primarily based on mapping using Entrez Gene identifiers.
    """

    bioc = "org.Ss.eg.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Ss.eg.db_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Ss.eg.db/org.Ss.eg.db_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="1840341447de2711a97ac09f0c12d332a1c7eb7bfe79ff53b41aea0309e4194b",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
