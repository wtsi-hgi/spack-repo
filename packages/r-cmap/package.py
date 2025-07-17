# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmap(RPackage):
    """A data package containing annotation data for cMAP

    Annotation data file for cMAP assembled using data from public data repositories
    """

    bioc = "cMAP"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/cMAP_1.15.1.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/cMAP/cMAP_1.15.1.tar.gz",
    ]

    version(
        "1.15.1",
        sha256="3bf24aca1ce63ebff4ac0172467ecd8acbb0c1f8a240cd0f8b8abd7c44fdf15f",
    )

    depends_on("r@2.4:", type=("build", "run"))
