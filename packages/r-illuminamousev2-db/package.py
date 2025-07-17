# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminamousev2Db(RPackage):
    """Illumina MouseWG6v2 annotation data (chip illuminaMousev2)

    Illumina MouseWG6v2 annotation data (chip illuminaMousev2) assembled using data from public repositories
    """

    bioc = "illuminaMousev2.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/illuminaMousev2.db_1.26.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/illuminaMousev2.db/illuminaMousev2.db_1.26.0.tar.gz",
    ]

    version(
        "1.26.0",
        sha256="03864df588d7261db6923d0d7cccdd9bbb753ce60e4cdf92ba2bc3ea1318916f",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.1.2:", type=("build", "run"))
