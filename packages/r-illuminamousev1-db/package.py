# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminamousev1Db(RPackage):
    """Illumina MouseWG6v1 annotation data (chip illuminaMousev1)

    Illumina MouseWG6v1 annotation data (chip illuminaMousev1) assembled using data from public repositories
    """

    bioc = "illuminaMousev1.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/illuminaMousev1.db_1.26.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/illuminaMousev1.db/illuminaMousev1.db_1.26.0.tar.gz",
    ]

    version(
        "1.26.0",
        sha256="cf8a1cecfc1ec1164488b2b0b38b3f21e44f2cbf7bc041290fad2bc463fc5170",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.1.2:", type=("build", "run"))
