# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoe430aDb(RPackage):
    """Affymetrix Affymetrix MOE430A Array annotation data (chip moe430a)

    Affymetrix Affymetrix MOE430A Array annotation data (chip moe430a) assembled using data from public repositories
    """

    bioc = "moe430a.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/moe430a.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/moe430a.db/moe430a.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="832c0d8cafdc97c4001fdf8e1f74718db6228d2392394e5892bc5698237b89e1",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))
