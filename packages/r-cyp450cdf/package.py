# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCyp450cdf(RPackage):
    """cyp450cdf

    A package containing an environment representing the CYP450.CDF file.
    """

    bioc = "cyp450cdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/cyp450cdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/cyp450cdf/cyp450cdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="c061143e44e18b5d790e96bf18124e7bda2d491cb34dbff504ac6b4052b278d5",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
