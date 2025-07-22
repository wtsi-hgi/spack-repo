# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74cv2Db(RPackage):
    """Affymetrix Affymetrix MG_U74Cv2 Array annotation data (chip mgu74cv2)

    Affymetrix Affymetrix MG_U74Cv2 Array annotation data (chip mgu74cv2) assembled using data from public repositories
    """

    bioc = "mgu74cv2.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74cv2.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74cv2.db/mgu74cv2.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="994e4458174efa260a19d03e67a1f35ac06e6430399cbbf0bd42791123ce4b1c",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))
