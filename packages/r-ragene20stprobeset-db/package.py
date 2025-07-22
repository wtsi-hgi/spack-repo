# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRagene20stprobesetDb(RPackage):
    """Affymetrix ragene20 annotation data (chip ragene20stprobeset)

    Affymetrix ragene20 annotation data (chip ragene20stprobeset) assembled using data from public repositories
    """

    bioc = "ragene20stprobeset.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ragene20stprobeset.db_8.8.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ragene20stprobeset.db/ragene20stprobeset.db_8.8.0.tar.gz",
    ]

    version(
        "8.8.0",
        sha256="bff7539635e6742af7f6ed3282847b828601541aaccdffc5d2ba872926916c30",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))
