# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNugomm1a520177Db(RPackage):
    """Affymetrix nugomm1a520177 annotation data (chip nugomm1a520177)

    Affymetrix nugomm1a520177 annotation data (chip nugomm1a520177) assembled using data from public repositories
    """

    bioc = "nugomm1a520177.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/nugomm1a520177.db_3.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/nugomm1a520177.db/nugomm1a520177.db_3.4.0.tar.gz",
    ]

    version(
        "3.4.0",
        sha256="059f8575483d7754f0c5dca52f6bf51611aa9bd14030d41672338eef1f2c78e8",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.2.1:", type=("build", "run"))
