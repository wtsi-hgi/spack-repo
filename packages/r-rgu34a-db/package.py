# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgu34aDb(RPackage):
    """Affymetrix Affymetrix RG_U34A Array annotation data (chip rgu34a)

    Affymetrix Affymetrix RG_U34A Array annotation data (chip rgu34a) assembled using data from public repositories
    """

    bioc = "rgu34a.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rgu34a.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rgu34a.db/rgu34a.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="e6280a33c816e21e2ca09b0bcd4c7d6186d9b58f9d52b4ddec087ea0e24382da",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))
