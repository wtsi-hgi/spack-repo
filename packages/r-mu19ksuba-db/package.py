# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu19ksubaDb(RPackage):
    """Affymetrix Affymetrix Mu19KsubA Array annotation data (chip mu19ksuba)

    Affymetrix Affymetrix Mu19KsubA Array annotation data (chip mu19ksuba) assembled using data from public repositories
    """

    bioc = "mu19ksuba.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu19ksuba.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu19ksuba.db/mu19ksuba.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="9b8e4f0278e3b1df5494befa2333adba2b961976bb0585c7a13ab7bf56fe49cb",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))
