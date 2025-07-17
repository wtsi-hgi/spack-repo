# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlyDb0(RPackage):
    """Base Level Annotation databases for fly

    Base annotation databases for fly, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
    """

    bioc = "fly.db0"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/fly.db0_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/fly.db0/fly.db0_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="2f170e187d3ed3a41a80a810d5e9b604b178cb48cb1de685fbb1b4c665ca7ade",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/fly.db0_3.18.0.tar.gz",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
