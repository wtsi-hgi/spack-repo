# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanv4Db(RPackage):
    """Illumina HumanHT12v4 annotation data (chip illuminaHumanv4)

    Illumina HumanHT12v4 annotation data (chip illuminaHumanv4) assembled using data from public repositories
    """

    bioc = "illuminaHumanv4.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/illuminaHumanv4.db_1.26.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/illuminaHumanv4.db/illuminaHumanv4.db_1.26.0.tar.gz",
    ]

    version(
        "1.26.0",
        sha256="362848d6e78c7fa6206e1a4c68a4b68c1ea065267d550114837bc3b9d833ee85",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.1.2:", type=("build", "run"))
