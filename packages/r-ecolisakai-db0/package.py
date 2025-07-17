# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcolisakaiDb0(RPackage):
    """Base Level Annotation databases for E coli Sakai Strain

    Base annotation databases for E coli Sakai Strain, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
    """

    bioc = "ecoliSakai.db0"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ecoliSakai.db0_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ecoliSakai.db0/ecoliSakai.db0_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="9fbbe85bd912873b9a1b30ede51b37e79e1ae8b7975410d7d10f38ae64950a4e",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ecoliSakai.db0_3.18.0.tar.gz",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
