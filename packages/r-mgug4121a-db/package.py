# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgug4121aDb(RPackage):
    """Agilent Mouse annotation data (chip mgug4121a)

    Agilent Mouse annotation data (chip mgug4121a) assembled using data from public repositories
    """

    bioc = "mgug4121a.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgug4121a.db_3.2.3.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgug4121a.db/mgug4121a.db_3.2.3.tar.gz",
    ]

    version(
        "3.2.3",
        sha256="e533d3e5cb4898a1642a2edd857668100b7facca569dcfdf5f445a3465668724",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.3:", type=("build", "run"))
