# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumanDb0(RPackage):
    """Base Level Annotation databases for human

    Base annotation databases for human, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
    """

    bioc = "human.db0"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/human.db0_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/human.db0/human.db0_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="ee0774370fb3b3ee4de7660fe65760c0809b5fe3083fd2dcc6e6a40172d98446",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/human.db0_3.18.0.tar.gz",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
