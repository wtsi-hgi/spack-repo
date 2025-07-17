# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMouse4302Db(RPackage):
    """Affymetrix Affymetrix Mouse430_2 Array annotation data (chip mouse4302)

    Affymetrix Affymetrix Mouse430_2 Array annotation data (chip mouse4302) assembled using data from public repositories
    """

    bioc = "mouse4302.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mouse4302.db_3.13.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mouse4302.db/mouse4302.db_3.13.0.tar.gz",
    ]

    version(
        "3.13.0",
        sha256="9ae5334bba7572109d0ec5bd33baf2403ab3afad0373f6c055267923dd14c265",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))
