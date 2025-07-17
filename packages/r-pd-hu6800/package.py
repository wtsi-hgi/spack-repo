# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdHu6800(RPackage):
    """Platform Design Info for The Manufacturer's Name Hu6800

    Platform Design Info for The Manufacturer's Name Hu6800
    """

    bioc = "pd.hu6800"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.hu6800_3.12.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.hu6800/pd.hu6800_3.12.0.tar.gz",
    ]

    version(
        "3.12.0",
        sha256="bbca5c458e304e50834548c06167a2ca1282ec3522e8b494e273947eb702b21d",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.hu6800_3.12.0.tar.gz",
    )

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-biostrings@2.35.12:", type=("build", "run"))
    depends_on("r-rsqlite@1:", type=("build", "run"))
    depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
    depends_on("r-oligo@1.31.5:", type=("build", "run"))
    depends_on("r-dbi@0.3.1:", type=("build", "run"))
    depends_on("r-iranges@2.1.43:", type=("build", "run"))
    depends_on("r-s4vectors@0.5.22:", type=("build", "run"))
