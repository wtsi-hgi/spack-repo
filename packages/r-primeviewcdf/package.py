# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrimeviewcdf(RPackage):
    """primeviewcdf

    A package containing an environment representing the PrimeView.cdf file.
    """

    bioc = "primeviewcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/primeviewcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/primeviewcdf/primeviewcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="887c91b09a4bd5cced4a0239bea6bc0d92acf062a8887cd36982dea5a2a04362",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
