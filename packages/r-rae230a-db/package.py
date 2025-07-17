# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRae230aDb(RPackage):
    """Affymetrix Affymetrix RAE230A Array annotation data (chip rae230a)

    Affymetrix Affymetrix RAE230A Array annotation data (chip rae230a) assembled using data from public repositories
    """

    bioc = "rae230a.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rae230a.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rae230a.db/rae230a.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="fea78cab0e2527d662b0548a9cf47a2b89ecde5da0c9fab24aa1b08f7ae5ae8e",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))
