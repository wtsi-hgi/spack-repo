# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoex10stprobesetDb(RPackage):
    """Affymetrix moex10 annotation data (chip moex10stprobeset)

    Affymetrix moex10 annotation data (chip moex10stprobeset) assembled using data from public repositories
    """

    bioc = "moex10stprobeset.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/moex10stprobeset.db_8.8.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/moex10stprobeset.db/moex10stprobeset.db_8.8.0.tar.gz",
    ]

    version(
        "8.8.0",
        sha256="2d8f36c87413e9b54f968e30e3853e1fe3f0093fb887177c423b5162b3ba92a8",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))
