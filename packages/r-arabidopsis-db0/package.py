# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArabidopsisDb0(RPackage):
    """Base Level Annotation databases for arabidopsis

    Base annotation databases for arabidopsis, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
    """

    bioc = "arabidopsis.db0"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/arabidopsis.db0_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/arabidopsis.db0/arabidopsis.db0_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="6540aac2cf57aa81231da4a4cb460f1519c6b7d63ba92e8520ce2a837fde62b7",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/arabidopsis.db0_3.18.0.tar.gz",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
