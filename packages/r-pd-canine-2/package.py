# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdCanine2(RPackage):
    """Platform Design Info for The Manufacturer's Name Canine_2

    Platform Design Info for The Manufacturer's Name Canine_2
    """

    bioc = "pd.canine.2"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.canine.2_3.12.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.canine.2/pd.canine.2_3.12.0.tar.gz",
    ]

    version(
        "3.12.0",
        md5="bc918d1953a3c7ac7168b60a53405a93",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.canine.2_3.12.0.tar.gz",
    )

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-biostrings@2.35.12:", type=("build", "run"))
    depends_on("r-rsqlite@1:", type=("build", "run"))
    depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
    depends_on("r-oligo@1.31.5:", type=("build", "run"))
    depends_on("r-dbi@0.3.1:", type=("build", "run"))
    depends_on("r-iranges@2.1.43:", type=("build", "run"))
    depends_on("r-s4vectors@0.5.22:", type=("build", "run"))
