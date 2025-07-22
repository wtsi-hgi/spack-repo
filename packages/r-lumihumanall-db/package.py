# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLumihumanallDb(RPackage):
    """Illumina Human Illumina expression annotation data (chip lumiHumanAll)

    Illumina Human Illumina expression annotation data (chip lumiHumanAll) assembled using data from public repositories
    """

    bioc = "lumiHumanAll.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/lumiHumanAll.db_1.22.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/lumiHumanAll.db/lumiHumanAll.db_1.22.0.tar.gz",
    ]

    version(
        "1.22.0",
        sha256="a2c1bd766e756eb7e01cf196c1809c8a282a4c4caaf1482a0d1961b2c2a8c24e",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@2.10.1:", type=("build", "run"))
