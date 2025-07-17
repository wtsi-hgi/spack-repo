# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTest3cdf(RPackage):
    """test3cdf

    A package containing an environment representing the Test3.CDF file.
    """

    bioc = "test3cdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/test3cdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/test3cdf/test3cdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="90ac86eb75cefcbe81c87e1bda8a8a2d54766b2b9dd047061bc589323179a424",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
