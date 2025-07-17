# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgMmuEgDb(RPackage):
    """Genome wide annotation for Rhesus

    Genome wide annotation for Rhesus, primarily based on mapping using Entrez Gene identifiers.
    """

    bioc = "org.Mmu.eg.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Mmu.eg.db_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Mmu.eg.db/org.Mmu.eg.db_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="109899eb5b74a6bbb87fa40095c9254301e1463f738956e73e61e3bb7c3340e2",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
