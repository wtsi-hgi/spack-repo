# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWheatcdf(RPackage):
    """wheatcdf

    A package containing an environment representing the wheat.cdf file.
    """

    bioc = "wheatcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/wheatcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/wheatcdf/wheatcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="79a25c63c65054caef431293c67dbc51a13803a82cac690d24a56e4c63cbabbe",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
