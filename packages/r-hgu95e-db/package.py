# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95eDb(RPackage):
    """Affymetrix Affymetrix HG_U95E Array annotation data (chip hgu95e)

    Affymetrix Affymetrix HG_U95E Array annotation data (chip hgu95e) assembled using data from public repositories
    """

    bioc = "hgu95e.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95e.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95e.db/hgu95e.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="df1bb4a2b6640e22c0c9dcb134305ac2a3c79cf361e0caf53f371b1fed36c1dc",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))
