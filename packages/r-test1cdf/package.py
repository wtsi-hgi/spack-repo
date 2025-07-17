# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTest1cdf(RPackage):
    """test1cdf

    A package containing an environment representing the Test1.CDF file.
    """

    bioc = "test1cdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/test1cdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/test1cdf/test1cdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="24b3c71ad24287db8071ee16e50c549d247e7cd9ceb266d1bb095cb1c8cdb35a",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
