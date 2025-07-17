# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuex10sttranscriptclusterDb(RPackage):
    """Affymetrix huex10 annotation data (chip huex10sttranscriptcluster)

    Affymetrix huex10 annotation data (chip huex10sttranscriptcluster) assembled using data from public repositories
    """

    bioc = "huex10sttranscriptcluster.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/huex10sttranscriptcluster.db_8.8.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/huex10sttranscriptcluster.db/huex10sttranscriptcluster.db_8.8.0.tar.gz",
    ]

    version(
        "8.8.0",
        sha256="4084ec2d8e416ddac65c5a34121f4b4da2b3205f0d73a92070e72c0990d0f65d",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))
