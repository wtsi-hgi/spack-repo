# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdMta10(RPackage):
    """Platform Design Info for Affymetrix MTA-1_0

    Platform Design Info for Affymetrix MTA-1_0
    """

    bioc = "pd.mta.1.0"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.mta.1.0_3.12.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.mta.1.0/pd.mta.1.0_3.12.0.tar.gz",
    ]

    version(
        "3.12.0",
        md5="0f737b4f1f1353733e56e2df637f554b",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.mta.1.0_3.12.0.tar.gz",
    )

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-biostrings@2.35.12:", type=("build", "run"))
    depends_on("r-rsqlite@1:", type=("build", "run"))
    depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
    depends_on("r-oligo@1.31.5:", type=("build", "run"))
    depends_on("r-dbi@0.3.1:", type=("build", "run"))
    depends_on("r-iranges@2.1.43:", type=("build", "run"))
    depends_on("r-s4vectors@0.5.22:", type=("build", "run"))
