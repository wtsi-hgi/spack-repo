# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM10kcodDb(RPackage):
    """Codelink UniSet Mouse I Bioarray (~10 000 mouse gene targets) annotation data (chip m10kcod)

    Codelink UniSet Mouse I Bioarray (~10 000 mouse gene targets) annotation data (chip m10kcod) assembled using data from public repositories
    """

    bioc = "m10kcod.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/m10kcod.db_3.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/m10kcod.db/m10kcod.db_3.4.0.tar.gz",
    ]

    version(
        "3.4.0",
        sha256="5059506391d798410dcef55b9f106c3819111a7d6bfc20efa3dd8c12a3fc0e3b",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.2.1:", type=("build", "run"))
