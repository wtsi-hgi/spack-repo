# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShdzDb(RPackage):
    """SHDZ http://genome-www5.stanford.edu/ Annotation Data (SHDZ)

    SHDZ http://genome-www5.stanford.edu/ Annotation Data (SHDZ) assembled using data from public repositories
    """

    bioc = "SHDZ.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SHDZ.db_3.2.3.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/SHDZ.db/SHDZ.db_3.2.3.tar.gz",
    ]

    version(
        "3.2.3",
        sha256="bab75f442a5ebf6ac7907c44267160faf15cbb1871a2105b008cb8d1bff0fd1c",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))
