# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZebrafishDb0(RPackage):
    """Base Level Annotation databases for zebrafish

    Base annotation databases for zebrafish, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
    """

    bioc = "zebrafish.db0"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/zebrafish.db0_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/zebrafish.db0/zebrafish.db0_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="539b878c3999c48f0d664a980feb278fc3175d89b55adbc070d28c44cb0a2d63",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/zebrafish.db0_3.18.0.tar.gz",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
