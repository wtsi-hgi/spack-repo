# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRagene20sttranscriptclusterDb(RPackage):
    """Affymetrix ragene20 annotation data (chip ragene20sttranscriptcluster)

    Affymetrix ragene20 annotation data (chip ragene20sttranscriptcluster) assembled using data from public repositories
    """

    bioc = "ragene20sttranscriptcluster.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ragene20sttranscriptcluster.db_8.8.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ragene20sttranscriptcluster.db/ragene20sttranscriptcluster.db_8.8.0.tar.gz",
    ]

    version(
        "8.8.0",
        sha256="1034076b931a6a99070c176fe10f36e2fb8ae370bb43cdfb565ec3a581e724ae",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))
