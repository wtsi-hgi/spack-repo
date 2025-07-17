# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubdDb(RPackage):
    """Affymetrix Affymetrix Hu35KsubD Array annotation data (chip hu35ksubd)

    Affymetrix Affymetrix Hu35KsubD Array annotation data (chip hu35ksubd) assembled using data from public repositories
    """

    bioc = "hu35ksubd.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu35ksubd.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu35ksubd.db/hu35ksubd.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="0b3215327224093d58972997a2b8ee9e2f78697e1b3487676600e6c81184102f",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))
