# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMi16codDb(RPackage):
    """Codelink Mouse Inflammation 16 Bioarray annotation data (chip mi16cod)

    Codelink Mouse Inflammation 16 Bioarray annotation data (chip mi16cod) assembled using data from public repositories
    """

    bioc = "mi16cod.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mi16cod.db_3.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mi16cod.db/mi16cod.db_3.4.0.tar.gz",
    ]

    version(
        "3.4.0",
        sha256="02a9b0c60b7cacb4143d381e91f95daf92c605c42111efe56e709c6037bdc4ec",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.2.1:", type=("build", "run"))
