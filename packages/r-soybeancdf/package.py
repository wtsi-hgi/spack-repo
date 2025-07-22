# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoybeancdf(RPackage):
    """soybeancdf

    A package containing an environment representing the Soybean.cdf file.
    """

    bioc = "soybeancdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/soybeancdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/soybeancdf/soybeancdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="480ffd0c3d941a7487d91bfeb8bfc3fcf29339149f38f3833147a04a75eb9cb6",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
