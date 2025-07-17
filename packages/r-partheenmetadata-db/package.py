# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartheenmetadataDb(RPackage):
    """PartheenMetaData http://swegene.onk.lu.se Annotation Data (PartheenMetaData)

    PartheenMetaData http://swegene.onk.lu.se Annotation Data (PartheenMetaData) assembled using data from public repositories
    """

    bioc = "PartheenMetaData.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/PartheenMetaData.db_3.2.3.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/PartheenMetaData.db/PartheenMetaData.db_3.2.3.tar.gz",
    ]

    version(
        "3.2.3",
        sha256="bf658faa7e1c0f8eb49f9b94edfd2d53663d137d47eaf3f69ccf0d7d56616734",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))
