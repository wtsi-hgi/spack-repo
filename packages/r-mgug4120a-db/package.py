# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgug4120aDb(RPackage):
    """Agilent annotation data (chip mgug4120a)

    Agilent annotation data (chip mgug4120a) assembled using data from public repositories
    """

    bioc = "mgug4120a.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgug4120a.db_3.2.3.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgug4120a.db/mgug4120a.db_3.2.3.tar.gz",
    ]

    version(
        "3.2.3",
        sha256="7d035786f014f0cd710083a5170ddaea79f46c6b2e8310893422794e38bfdfe2",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.3:", type=("build", "run"))
