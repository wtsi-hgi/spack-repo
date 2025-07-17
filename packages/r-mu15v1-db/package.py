# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu15v1Db(RPackage):
    """FHCRC Genomics Shared Resource Mu15v1 Annotation Data (Mu15v1)

    FHCRC Genomics Shared Resource Mu15v1 Annotation Data (Mu15v1) assembled using data from public repositories
    """

    bioc = "Mu15v1.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Mu15v1.db_3.2.3.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/Mu15v1.db/Mu15v1.db_3.2.3.tar.gz",
    ]

    version(
        "3.2.3",
        sha256="9f06fe5d624a36bf4f48a38d1628757af23986ecd4418c96927179d3d7c49061",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.3:", type=("build", "run"))
