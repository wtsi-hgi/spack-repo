# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu11ksubbDb(RPackage):
    """Affymetrix Affymetrix Mu11KsubB Array annotation data (chip mu11ksubb)

    Affymetrix Affymetrix Mu11KsubB Array annotation data (chip mu11ksubb) assembled using data from public repositories
    """

    bioc = "mu11ksubb.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu11ksubb.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu11ksubb.db/mu11ksubb.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="9cc036efda366a61e950cfc066b803a77905f30aaea06016af6ae733485cd47c",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))
