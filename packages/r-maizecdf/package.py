# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaizecdf(RPackage):
    """maizecdf

    A package containing an environment representing the Maize.cdf file.
    """

    bioc = "maizecdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/maizecdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/maizecdf/maizecdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="a4c5f6c7fdcae0aa116b4c684773d56f802f3b0c2be861a4f99c600de52bdf79",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
