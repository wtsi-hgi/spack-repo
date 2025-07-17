# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeast2cdf(RPackage):
    """yeast2cdf

    A package containing an environment representing the Yeast_2.cdf file.
    """

    bioc = "yeast2cdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/yeast2cdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/yeast2cdf/yeast2cdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="8923c2a508106a3b14bc0dc8f51bc2a56bde5b7a6a83dec9b66ea19ea8dac830",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
