# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcoliasv2cdf(RPackage):
    """ecoliasv2cdf

    A package containing an environment representing the Ecoli_ASv2.CDF file.
    """

    bioc = "ecoliasv2cdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ecoliasv2cdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ecoliasv2cdf/ecoliasv2cdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="5bf91f4c54f9875c2e3e8895dd2c0f63c80403632a13e1d954bf3e9cb482269a",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
