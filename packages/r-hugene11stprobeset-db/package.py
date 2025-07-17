# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHugene11stprobesetDb(RPackage):
    """Affymetrix hugene11 annotation data (chip hugene11stprobeset)

    Affymetrix hugene11 annotation data (chip hugene11stprobeset) assembled using data from public repositories
    """

    bioc = "hugene11stprobeset.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hugene11stprobeset.db_8.8.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hugene11stprobeset.db/hugene11stprobeset.db_8.8.0.tar.gz",
    ]

    version(
        "8.8.0",
        sha256="e7690b0c366472bc730edf168e6b34b957177af0b6163e7fb3b585a74c244e46",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))
