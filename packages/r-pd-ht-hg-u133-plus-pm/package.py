# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdHtHgU133PlusPm(RPackage):
    """Platform Design Info for The Manufacturer's Name HT_HG-U133_Plus_PM

    Platform Design Info for The Manufacturer's Name HT_HG-U133_Plus_PM
    """

    bioc = "pd.ht.hg.u133.plus.pm"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.ht.hg.u133.plus.pm_3.12.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.ht.hg.u133.plus.pm/pd.ht.hg.u133.plus.pm_3.12.0.tar.gz",
    ]

    version(
        "3.12.0",
        sha256="2241ad5e3c4b7eae5a132e5962e750f4d13efa74000dd7d804ec7b245a700080",
    )

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-biostrings@2.35.12:", type=("build", "run"))
    depends_on("r-rsqlite@1:", type=("build", "run"))
    depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
    depends_on("r-oligo@1.31.5:", type=("build", "run"))
    depends_on("r-dbi@0.3.1:", type=("build", "run"))
    depends_on("r-iranges@2.1.43:", type=("build", "run"))
    depends_on("r-s4vectors@0.5.22:", type=("build", "run"))
