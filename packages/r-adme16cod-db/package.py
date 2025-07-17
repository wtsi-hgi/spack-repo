# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdme16codDb(RPackage):
    """Codelink ADME Rat 16-Assay Bioarray annotation data (chip adme16cod)

    Codelink ADME Rat 16-Assay Bioarray annotation data (chip adme16cod) assembled using data from public repositories
    """

    bioc = "adme16cod.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/adme16cod.db_3.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/adme16cod.db/adme16cod.db_3.4.0.tar.gz",
    ]

    version(
        "3.4.0",
        sha256="78674152312bee85aec2f2e65b0b594ee2df5c0861355501d0ff1b9a69d0c9ee",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-rn-eg-db@3.2.1:", type=("build", "run"))
