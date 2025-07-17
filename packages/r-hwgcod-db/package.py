# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHwgcodDb(RPackage):
    """Codelink Human Whole Genome Bioarray (~55 000 human genes) annotation data (chip hwgcod)

    Codelink Human Whole Genome Bioarray (~55 000 human genes) annotation data (chip hwgcod) assembled using data from public repositories
    """

    bioc = "hwgcod.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hwgcod.db_3.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hwgcod.db/hwgcod.db_3.4.0.tar.gz",
    ]

    version(
        "3.4.0",
        sha256="4b54ced8dd3bc28bdb7a22589e085acb13877f35715e2cae745f30cd484a3e0c",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.2.1:", type=("build", "run"))
