# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminamousev1p1Db(RPackage):
    """Illumina MouseWG6v1p1 annotation data (chip illuminaMousev1p1)

    Illumina MouseWG6v1p1 annotation data (chip illuminaMousev1p1) assembled using data from public repositories
    """

    bioc = "illuminaMousev1p1.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/illuminaMousev1p1.db_1.26.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/illuminaMousev1p1.db/illuminaMousev1p1.db_1.26.0.tar.gz",
    ]

    version(
        "1.26.0",
        sha256="e19f12982f108da2678ab8d12d5d4cc9a8c2d14bbe27736530e3243358e6b8eb",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.1.2:", type=("build", "run"))
