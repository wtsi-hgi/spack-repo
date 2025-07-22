# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgPtEgDb(RPackage):
    """Genome wide annotation for Chimp

    Genome wide annotation for Chimp, primarily based on mapping using Entrez Gene identifiers.
    """

    bioc = "org.Pt.eg.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Pt.eg.db_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Pt.eg.db/org.Pt.eg.db_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="cefb919bfa61ebbc931b8b42a02543cd8f35fe41a13f3392faae34225da0603b",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
