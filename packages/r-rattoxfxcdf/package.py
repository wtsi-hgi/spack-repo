# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRattoxfxcdf(RPackage):
    """rattoxfxcdf

    A package containing an environment representing the RatToxFX.cdf file.
    """

    bioc = "rattoxfxcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rattoxfxcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rattoxfxcdf/rattoxfxcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="167bd2efb1bfc73250c65636108994ae845683e2ba235ceafa425adb95a30461",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
